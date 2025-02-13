import httpx
from typing import Dict, Optional

DOWNLOADER_API = "http://yt_app:5000/api/download"

async def download_media(url: str, media_type: str) -> Optional[Dict]:
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                DOWNLOADER_API,
                json={
                    "url": url, 
                    "type": media_type
                }
            )

            print(f"Respuesta del downloader: {response.status_code}") 
            
            if response.status_code == 200:
                data = await response.json()
                print(f"Datos recibidos: {data}")  # Debug
                return {
                    "path": f"/shared/{data['filename']}",
                    "title": data["title"]
                }
            else:
                print(f"❌ Error del servidor: {response.text}")  # Debug
                return None
            
    except Exception as e:
        print(f"Error de descarga: {str(e)}")
        return None