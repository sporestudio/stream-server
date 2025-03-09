#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import Mock, patch
from yt_app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_missing_url(client):
    response = client.post('/api/download', json={'type': 'video'})
    assert response.status_code == 400
    assert 'error' in response.json

@patch('yt_app.main.YoutubeDL')
def test_invalid_url(mock_ydl, client):
    mock_instance = Mock()
    mock_instance.extract_info.side_effect = Exception("Invalid URL")
    mock_ydl.return_value.__enter__.return_value = mock_instance

    response = client.post('/api/download', json={
        'url': 'invalid_url',
        'type': 'video'
    })
    
    assert response.status_code == 500
    assert 'Error extracting info' in response.json['error']

@patch('yt_app.main.YoutubeDL')
@patch('yt_app.main.datetime')
def test_successful_video_download(mock_datetime, mock_ydl, client):
    mock_datetime.now.return_value.strftime.return_value = '2024-01-01_12-00-00'
    mock_info = {'title': 'Test Video', 'ext': 'mp4'}
    
    mock_instance = Mock()
    mock_instance.extract_info.return_value = mock_info
    mock_instance.prepare_filename.return_value = '/shared/test_video-2024-01-01_12-00-00.mp4'
    mock_ydl.return_value.__enter__.return_value = mock_instance

    response = client.post('/api/download', json={
        'url': 'https://youtube.com/watch?v=abc123',
        'type': 'video'
    })
    
    assert response.status_code == 200
    assert 'test_video-2024-01-01_12-00-00.mp4' in response.json['filename']

@patch('yt_app.main.YoutubeDL')
def test_audio_download_format(mock_ydl, client):
    
    mock_instance = Mock()
    mock_instance.extract_info.return_value = {'title': 'Test Audio', 'ext': 'mp3'}
    mock_instance.prepare_filename.return_value = "/shared/test_audio.mp3"  
    mock_ydl.return_value.__enter__.return_value = mock_instance

    
    response = client.post('/api/download', json={
        'url': 'valid_url',
        'type': 'audio'
    })
    
    
    ydl_opts = mock_ydl.call_args[0][0]
    assert ydl_opts['format'] == 'bestaudio'
    assert response.json['filename'] == 'test_audio.mp3' 

@patch('yt_app.main.YoutubeDL')
def test_download_error(mock_ydl, client):
    mock_instance = Mock()
    mock_instance.extract_info.return_value = {'title': 'Test'}
    mock_instance.download.side_effect = Exception("Download failed")
    mock_ydl.return_value.__enter__.return_value = mock_instance

    response = client.post('/api/download', json={
        'url': 'valid_url',
        'type': 'video'
    })
    
    assert response.status_code == 500
    assert 'Download failed' in response.json['error']


@patch('yt_app.main.slugify')
def test_filename_generation(mock_slugify, client):
    mock_slugify.return_value = 'slugified-title'
    
    with patch('yt_app.main.datetime') as mock_datetime:
        mock_datetime.now.return_value.strftime.return_value = 'timestamp'
        
        with patch('yt_app.main.YoutubeDL') as mock_ydl:
            
            mock_instance = Mock()
            mock_instance.extract_info.return_value = {
                'title': 'Test Video',
                'ext': 'mp4',
                '_filename': 'video.mp4'  
            }
            mock_instance.prepare_filename.return_value = "/shared/slugified-title-timestamp.mp4"  
            mock_ydl.return_value.__enter__.return_value = mock_instance
            
            response = client.post('/api/download', json={
                'url': 'valid_url',
                'type': 'video'
            })
    
    
    assert response.status_code == 200
    assert 'filename' in response.json
    assert 'slugified-title-timestamp.mp4' == response.json['filename']