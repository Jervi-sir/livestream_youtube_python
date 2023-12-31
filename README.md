# 24/7 YouTube Live Streaming using FFmpeg

This project aims to automate 24/7 video streaming to YouTube using FFmpeg. The script monitors a folder (and its subfolders) for new video files and then streams them live to a pre-configured YouTube channel. This script is intended to run on Windows.

### note:
This script is generated by GPT4, and this is best what I got so far from multiple attempts prompts, stable and covers most issues the script might go throught

## Requirements

- Python 3.x
- FFmpeg installed and added to PATH
- YouTube channel with live streaming enabled
- Stream key for your YouTube live event

## Dependencies

To install project dependencies, run:

```bash
pip install watchdog
```

## Setup

1. Clone this repository.
```
git clone https://github.com/Jervi-sir/livestream_youtube_python.git
```

2. Change into the directory.
```
cd yourrepository
```

3. Modify the folder_to_watch, youtube_url, and stream_key variables in your_script.py:
```
folder_to_watch = "path/to/your/folder"
youtube_url = "rtmp://a.rtmp.youtube.com/live2"
stream_key = "your_stream_key_here"
```

## Usage

Run the script using:
```
python your_script.py
```
Replace your_script.py with the name you have given to the script file.


## Features

- Monitors a specified folder and its subfolders for new .mp4 video files
- Streams video files to YouTube in a concatenated playlist
- Streams video at 1080p resolution
- Handles bitrate and buffer size for optimal video quality

## Known Issues

- If a new video is added while FFmpeg is running, the script will detect it but won't include it in the ongoing stream. You would have to restart the script to include the new video.


## Contribution

Feel free to open issues and pull requests!

## License

This project is licensed under the MIT License.


