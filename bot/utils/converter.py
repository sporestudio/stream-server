import asyncio
from ffmpeg.asyncio import FFmpeg
import os

async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0] 
    output_path = f"{base_name}.m3u8"

    try:
        process = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-i", input_path,
            "-c:v", "libx264",
            "-profile:v", "baseline",
            "-pix_fmt", "yuv420p",
            "-preset", "veryfast",
            "-b:v", "800k",
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "44100",
            "-ac", "2",
            "-f", "hls",
            "-hls_time", "10",
            "-hls_list_size", "0",
            "-hls_segment_filename", f"{base_name}_%03d.ts",
            output_path
        )

        await process.wait()
        return output_path

        '''
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(input_path)
            .output(
                output_path,
                {"codec:v": "libx264", "filter:v": "scale=1280:-1"},
                preset="ultrafast",
                crf=24,
            )
        )

        await ffmpeg.execute()
        return output_path
        '''

    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")
    

async def convert_to_mp3(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0]
    output_path = f"{base_name}.mp3"

    try:
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(input_path)
            .output(
                output_path,
                format="mp3",          
                acodec="libmp3lame",     
                **{"b:a": "128k",      
                   "ar": "44100",      
                   "ac": "2"} 
            )
        )

        await ffmpeg.execute()
        return output_path

    except Exception as e:
        raise RuntimeError(f"Error in mp3 conversion: {str(e)}")

    
    