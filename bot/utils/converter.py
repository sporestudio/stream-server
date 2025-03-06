import asyncio
import ffmpeg
import os


async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0] 
    output_path = f"{base_name}.m3u8"

    try:
        process = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-y",                   
            "-i", input_path,
            "-c:v", "libx264",
            "-preset", "superfast",
            "-tune", "zerolatency",
            "-crf", "23",
            "-g", "60",             
            "-keyint_min", "60",
            "-sc_threshold", "0",
            "-c:a", "aac",
            "-ar", "44100",
            "-ac", "1",
            "-f", "hls",
            "-hls_time", "4",
            "-hls_list_size", "0",
            "-hls_flags", "delete_segments",
            "-threads", "0",
            output_path            
        )

        await process.wait()
        return output_path
    
    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")

  

async def convert_to_ogg(input_path: str) -> str:
    output_path = input_path.rsplit(".", 1)[0] + ".ogg"

    try:
        ffmpeg_command = await asyncio.create_subprocess_exec(
            "ffmpeg", "-y",
            "-i", input_path,
            "-vn",               
            "-acodec", "libvorbis",
            "-b:a", "128k",
            output_path
        )

        await ffmpeg_command.wait() 
        return output_path

    except Exception as e:
        raise RuntimeError(f"Error in mp3 conversion: {str(e)}")
