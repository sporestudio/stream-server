import os

def get_stream_url(filename: str, media_type: str) -> str:
    filename = os.path.basename(filename)

    if media_type == "video":
        base_url = "http://localhost/video.html?stream=http://localhost/hls/"
        return f"{base_url}{filename}"
    else:
        base_url = "http://localhost/audio/"
    return f"{base_url}{filename}"