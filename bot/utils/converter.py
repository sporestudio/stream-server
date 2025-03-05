import asyncio
from ffmpeg.asyncio import FFmpeg
import os

'''
async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0]
    # Asegúrate de que el directorio de salida exista:
    output_dir = os.path.dirname(base_name)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # Definir el path del manifest (output_path)
    output_path = f"{base_name}.m3u8"
    
    process = await asyncio.create_subprocess_exec(
        "ffmpeg",
        "-i", input_path,
        "-c:v", "copy",
        "-start_number", "0",
        "-f", "hls",
        "-hls_time", "10",
        "-hls_list_size", "0",
        "-hls_segment_filename", f"{base_name}_%03d.ts",
        output_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        error_msg = stderr.decode()
        raise Exception(f"ffmpeg failed with error: {error_msg}")
    
    return output_path
'''


async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0] 
    output_path = f"{base_name}.m3u8"

    try:
        process = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-i", input_path,
            "-c:v", "libx264",
            "-profile:v", "main",
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
    
    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")

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
  

async def convert_to_ogg(input_path: str) -> str:
    output_path = input_path.rsplit(".", 1)[0] + ".ogg"

    try:
        ffmpeg_command = await asyncio.create_subprocess_exec(
            "ffmpeg", "-y",
            "-i", input_path,
            "-vn",                # Sin video
            "-acodec", "libvorbis",
            "-b:a", "128k",
            output_path
        )

        await ffmpeg_command.wait() 
        return output_path

    except Exception as e:
        raise RuntimeError(f"Error in mp3 conversion: {str(e)}")

    
    