import asyncio
import ffmpeg
import os

async def convert_to_hls(input_path: str) -> str:
    base_name = os.path.splitext(input_path)[0]
    output_path = f"{base_name}.m3u8"
    
    try:
        stream = ffmpeg.input(input_path)
        
        stream = stream.output(
            output_path,
            **{
                'c:v': 'libx264',
                'preset': 'superfast',
                'tune': 'zerolatency',
                'crf': '23',
                'x264-params': 'keyint=60:min-keyint=60:scenecut=0',
                'g': '60',
                'c:a': 'aac',
                'ar': '44100',
                'ac': '1',
                'f': 'hls',
                'hls_time': '4',
                'hls_list_size': '0',
                'hls_flags': 'delete_segments',
                'threads': '0'
            }
        ).overwrite_output()
        
        cmd = stream.compile()
        
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
       
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
            raise RuntimeError(f"FFmpeg error: {stderr.decode('utf-8')}")
            
        return stdout
        
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Conversion error: {str(e)}")

  

async def convert_to_ogg(input_path: str) -> str:
    output_path = input_path.rsplit(".", 1)[0] + ".ogg"

    try:
        stream = ffmpeg.input(input_path)

        stream = stream.output(
            output_path,
            **{
                'c:a': 'libvorbis',
                'b:a': '128k'
            }
        ).overwrite_output()

        cmd = stream.compile()

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise RuntimeError(f"FFmpeg error: {stderr.decode('utf-8')}")
        return stdout
    
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Error in mp3 conversion: {str(e)}")