"""
Pytest fixtures and config.

"""

import asyncio
import pytest

import aioipfsapi
from .server import IPFSServer, app


@pytest.fixture()
def event_loop():
    loop = asyncio.new_event_loop()

    yield loop


@pytest.fixture()
def ipfs_server(request):
    ipfs_server = IPFSServer(
        aioipfsapi.DEFAULT_HOST, aioipfsapi.DEFAULT_PORT, app
    )
    ipfs_server.start()

    request.addfinalizer(ipfs_server.stop)

    return ipfs_server


@pytest.fixture()
def ipfs_client(event_loop):

    client = aioipfsapi.AioClient(loop=event_loop

    )

    return client
