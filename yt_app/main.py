from flask import Flask, jsonify, request
from yt_dlp import YoutubeDL
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
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best' if media_type == 'video' else 'bestaudio',
            'outtmpl': os.path.join(SHARED_VOLUME, f'{str(uuid.uuid4())}.%(ext)s'),  
            'quiet': True, 
            'no_warnings': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return jsonify({
            "filename": os.path.basename(filename),
            "title": info.get('title', 'Unknown'),
            "type": media_type
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)