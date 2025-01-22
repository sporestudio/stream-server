from pytubefix import YouTube

def download_video(url, quality='highest'):
    yt = YouTube(url)

    if quality == 'highest':
        stream = yt.streams.get_highest_resolution()
    elif quality == 'lowest':
        stream = yt.streams.get_lowest_resolution()
    elif quality == 'audio':
        stream = yt.streams.filter(only_audio=True).first()
    else:
        raise ValueError("Calidad inválida seleccionada")
    
    output_path = f'/downloads/{stream.default_filename}'
    stream.download(output_path)
    return output_path
