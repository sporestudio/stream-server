def get_stream_url(file_path: str, media_type: str) -> str:
    filename = file_path.split("/")[-1]

    if media_type == "video":
        return f"https://localhost:8080/hls/{filename}"
    elif media_type == "audio":
        return f"https://localhost:8080/{filename}"
    else:
        raise ValueError("Media type not valid.")