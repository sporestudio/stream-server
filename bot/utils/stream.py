import os

def get_stream_url(filename: str, media_type: str) -> str:
    filename = os.path.basename(filename)

    if media_type == "video":
        base_url = "https://stream.sporestudio.me/video/"
        return f"{base_url}{filename}"
    else:
        base_url = "https://stream.sporestudio.me/audio"
    return f"{base_url}"