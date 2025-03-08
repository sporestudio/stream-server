import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class AudioFileHandler(FileSystemEventHandler):
    def __init__(self, shared_dir, playlist_file):
        self.shared_dir = shared_dir
        self.playlist_file = playlist_file
        self.update_playlist()

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.ogg'):
            self.update_playlist()

    def update_playlist(self):
        with open(self.playlist_file, 'w') as playlist:
            for root, _, files in os.walk(self.shared_dir):
                for file in files:
                    if file.endswith('.ogg'):
                        file_path = os.path.join(root, file)
                        playlist.write(f"{file_path}\n")
                        

if __name__ == "__main__":
    shared_dir = "/shared"
    playlist_file = "/var/lib/ices2/playlist"

    event_handler = AudioFileHandler(shared_dir, playlist_file)
    observer = Observer()
    observer.schedule(event_handler, path=shared_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()