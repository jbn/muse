import os.path
import subprocess
from urllib.parse import urlparse, parse_qs
from flask import Flask, request
from flask.ext.autoindex import AutoIndex
app = Flask(__name__)

DOWNLOAD_DIR = os.path.join(os.path.curdir, "downloads")

AutoIndex(app, browse_root=DOWNLOAD_DIR)

DEFAULT_CMD = ["youtube-dl",
               "--extract-audio",
               "--audio-format", "mp3",
               "--audio-quality", "9",
               "-o", "downloads/%(title)s.%(ext)s"]

def fetch(youtube_id):
    subprocess.check_call(DEFAULT_CMD + [youtube_id])


def get_video_id(youtube_url):
    return parse_qs(urlparse(youtube_url).query)['v'][0]


@app.route('/save')
def save_page():
    url = request.args.get("youtube_url")

    if url:
        fetch(get_video_id(url))

    return 'ok'


if __name__ == "__main__":
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    app.run(port=1994, debug=True)  # Because, you know, 1994 and Alt Rock. 
