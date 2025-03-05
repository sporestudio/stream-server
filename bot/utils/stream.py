import os

def get_stream_url(filename: str, media_type: str) -> str:
    filename = os.path.basename(filename)

    if media_type == "video":
        vlc_url = "https://stream.sporestudio.me/hls/"
        web_url = "https://stream.sporestudio.me/video/"
        return f"VLC url: {vlc_url}{filename}\n\nWeb url: {web_url}"
    else:
        base_url = "https://stream.sporestudio.me/audio"
    return f"{base_url}"