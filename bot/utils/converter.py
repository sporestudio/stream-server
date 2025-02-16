import asyncio
import ffmpeg
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
    
    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")