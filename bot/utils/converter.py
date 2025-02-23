import asyncio
from ffmpeg.asyncio import FFmpeg
import os

async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0] 
    output_path = f"{base_name}.m3u8"

    try:
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

    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")
    

async def convert_to_mp3(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0]
    output_path = f"{base_name}.mp3"

    try:
        ffmpeg = (
            FFmpeg()
        )
    except Exception as e:
        raise RuntimeError(f"Error in mp3 conversion: {str(e)}")

    
    