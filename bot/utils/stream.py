def get_stream_url(file_path: str, media_type: str) -> str:
    filename = file_path.split("/")[-1]

    if media_type == "video":
        return f"http://nginx:8080/hls/{filename}"
    elif media_type == "audio":
        return f"http://icecast:8000/{filename}"
    else:
        raise ValueError("Media type not valid.")