#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from yt_dlp import YoutubeDL
from slugify import slugify
import datetime
import os


# creating the instance for the app #
app = Flask(__name__)


SHARED_VOLUME = "/shared"


@app.route('/api/download', methods=['POST'])
def api_download():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    url = data.get('url')
    media_type = data.get('type')
    

    try:
        with YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True}) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": f"Error extracting info: {str(e)}"}), 500
    
    title = info.get('title', 'unknown')

    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename_template = f"{slugify(title)}-{now}.%(ext)s"

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best' if media_type == 'video' else 'bestaudio',
            'outtmpl': os.path.join(SHARED_VOLUME, filename_template),  
            'quiet': True, 
            'no_warnings': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            filename = ydl.prepare_filename(info)

        return jsonify({
            "filename": os.path.basename(filename),
            "title": title,
            "type": media_type
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)