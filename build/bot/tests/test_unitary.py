#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import httpx
from bot.utils.downloader import download_media
from anyio import create_task_group, run

@pytest.mark.asyncio
async def test_download_media_success(monkeypatch):
    class DummyResponse:
        status_code = 200

        def json(self):
            return {"filename": "dummy.mp4", "title": "Dummy Title"}

        @property
        def text(self):
            return "dummy response"

    async def dummy_post(*args, **kwargs):
        return DummyResponse()

    class DummyClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, *args, **kwargs):
            return await dummy_post(*args, **kwargs)

    monkeypatch.setattr(httpx, "AsyncClient", lambda timeout: DummyClient())

    result = await download_media("https://www.youtube.com/watch?v=dummy", "video")
    assert result is not None
    assert result["path"] == "/shared/dummy.mp4"
    assert result["title"] == "Dummy Title"

@pytest.mark.asyncio
async def test_download_media_failure(monkeypatch):
    class DummyResponse:
        status_code = 404

        @property
        def text(self):
            return "Not Found"

    async def dummy_post(*args, **kwargs):
        return DummyResponse()

    class DummyClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, *args, **kwargs):
            return await dummy_post(*args, **kwargs)

    monkeypatch.setattr(httpx, "AsyncClient", lambda timeout: DummyClient())

    result = await download_media("https://www.youtube.com/watch?v=dummy", "video")
    assert result is None