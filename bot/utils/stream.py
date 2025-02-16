import os

def get_stream_url(filename: str, media_type: str) -> str:
    filename = os.path.basename(filename)
    base_url = "http://localhost/hls/"
    return f"{base_url}{filename}"

