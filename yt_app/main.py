from flask import Flask, jsonify, request
from yt_app.downloader import download_video
import os


# creating the instance for the app #
app = Flask(__name__)


@app.route('/api/download', methods=['POST'])
def api_download():
    data = request.json
    url = data.get('url')
    quality = data.get('quality', 'highest')

    try:
        output_path = download_video(url, quality)
        return jsonify({'success': True, 'path': output_path})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)