def get_stream_url(file_path: str, media_type: str) -> str:
    """
    Genera la URL pública para acceder al archivo HLS.

    Args:
        filename (str): Nombre del archivo .m3u8 generado.

    Returns:
        str: URL completa para acceder al stream HLS.
    """
    base_url = "http://localhost/hls/" 
    return f"{base_url}{filename}"


