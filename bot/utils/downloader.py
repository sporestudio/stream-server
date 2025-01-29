import httpx
from typing import Dict, Optional

DOWNLOADER_API = "http://downloader:5000/api/download"

async def download_media(url: str, media_type: str) -> Optional[Dict]:
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                DOWNLOADER_API,
                json={"url": url, "type": media_type}
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "path": f"/shared_media/{data['filename']}",
                    "title": data["title"]
                }
            return None
            
    except Exception as e:
        print(f"Error de descarga: {str(e)}")
        return None