"""
Pytest fixtures and config.

"""

import asyncio
import pytest

import aioipfsapi


@pytest.fixture()
def event_loop():
    loop = asyncio.new_event_loop()

    yield loop


@pytest.fixture()
def ipfs_client(event_loop):

    client = aioipfsapi.AioClient(loop=event_loop)

    return client
