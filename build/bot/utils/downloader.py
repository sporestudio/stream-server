from typing import Dict, Optional
import httpx


DOWNLOADER_API = "http://yt-app:5000/api/download"

async def download_media(url: str, media_type: str) -> Optional[Dict]:
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                DOWNLOADER_API,
                json={"url": url, "type": media_type}
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()  
                except Exception as e:
                    return None

                return {
                    "path": f"/shared/{data['filename']}",
                    "title": data["title"]
                }
            else:
                return None
    except Exception as e:
        return None
