import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.folder_to_watch, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def process(event):
        print(f'New video {event.src_path} detected.')
        # Update your playlist, or change the FFmpeg command to include the new video

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

def ffmpeg_stream(folder_to_watch, youtube_url, stream_key):
    playlist = []
    for root, dirs, files in os.walk(folder_to_watch):
        for file in files:
            if file.endswith(".mp4"):
                playlist.append(os.path.join(root, file))

    playlist_str = '|'.join(playlist)
    ffmpeg_command = [
      'ffmpeg',
      '-re',
      '-stream_loop', '-1',
      '-i', f"concat:{playlist_str}",
      '-vf', 'scale=1920:1080',  # scale video to 1080p
      '-b:v', '6000k',  # video bitrate
      '-maxrate', '6000k',
      '-bufsize', '12000k',
      '-acodec', 'aac',  # audio codec
      '-ar', '44100',  # audio rate
      '-ab', '192k', # audio bitrate
      '-f', 'flv', f"{youtube_url}/{stream_key}"
    ]

    subprocess.Popen(ffmpeg_command)

if __name__ == '__main__':
    folder_to_watch = "Videos"
    youtube_url = "rtmp://a.rtmp.youtube.com/live2"
    stream_key = "5ety-wwuk-vpv5-8a1d-evku"

    # Start streaming
    ffmpeg_stream(folder_to_watch, youtube_url, stream_key)

    # Watch for new files
    watch = Watcher(folder_to_watch)
    watch.run()
