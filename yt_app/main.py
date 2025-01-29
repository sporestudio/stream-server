from flask import Flask, jsonify, request
from pytubefix import YouTube
import uuid
import os


# creating the instance for the app #
app = Flask(__name__)


SHARED_VOLUME = "/shared"


@app.route('/api/download', methods=['POST'])
def api_download():
    data = request.json
    url = data.get('url')
    media_type = data.get('type')

    try:
        yt = YouTube(url)
        unique_id = str(uuid.uuid4())

        if media_type == 'video':
            stream = yt.streams.get_highest_resolution()
            filename = f'{unique_id}.mp4'
        elif media_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
            filename = f'{unique_id}.mp3'
        else:
            return jsonify({
                "error": "Type no valid"
            }), 400

        filepath = os.path.join(SHARED_VOLUME, filename)
        stream.download(output_path=SHARED_VOLUME, filename=filename)

        return jsonify({
            "filename": filename,
            "title": yt.title,
            "type": media_type
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)