import os

def update_playlist(shared: str, playlist_file: str):
    with open(playlist_file, 'w') as playlist:
        for root, _, files in os.walk(shared_dir):
            for file in files:
                if file.endswith('.ogg'):
                    file_path = os.path.join(root, file)
                    playlist.write(f"{file_path}\n")


if __name__ == "__main__":
    shared_dir = "/shared"
    playlist_file = "/var/lib/ices2/playlist"
    update_playlist(shared_dir, playlist_file)