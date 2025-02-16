import os
import logging
from typing import Dict, Optional
import httpx

logger = logging.getLogger(__name__)

DOWNLOADER_API = "http://yt-app:5000/api/download"

async def download_media(url: str, media_type: str) -> Optional[Dict]:
    try:
        logger.info(f"Llamando a {DOWNLOADER_API} con URL: {url} y tipo: {media_type}")
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                DOWNLOADER_API,
                json={"url": url, "type": media_type}
            )
            logger.info(f"Respuesta del downloader: {response.status_code}")
            logger.info(f"Contenido de la respuesta: {response.text}")
            
            if response.status_code == 200:
                try:
                    data = response.json()  
                    logger.info(f"Datos recibidos: {data}")
                except Exception as e:
                    logger.error("Error al parsear el JSON de respuesta", exc_info=True)
                    return None

                return {
                    "path": f"/shared/{data['filename']}",
                    "title": data["title"]
                }
            else:
                logger.error(f"❌ Error del servidor: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        logger.exception(f"Error de descarga: {str(e)}")
        return None
