import pytest

from aioipfsapi import AioClient
from .server import IPFSServer

@pytest.fixture
def ipfs_server():
    ipfs_server = IPFSServer()
    ipfs_server.start()

    return ipfs_server

@pytest.fixture
def ipfs_client(ipfs_server):

    client = AioClient(
        ipfs_server.hostname, ipfs_server.port
    )
    return client
