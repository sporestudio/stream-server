import asyncio
import ffmpeg

async def convert_to_hls(input_path: str) -> str:
    output_path = f"{output_path}.m3u8"

    try:
        process = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-i", input_path,
            "-c:v", "copy",
            "-c:a", "copy",
            "-f", "hls",
            "-hls_time", "10",
            "-hls_list_size", "0",
            output_path
        )

        await process.wait()
        return output_path
    
    except Exception as e:
        raise RuntimeError(f"Error in hls conversion: {str(e)}")