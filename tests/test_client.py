import pytest

def test_version(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.id()
        assert content == {}

