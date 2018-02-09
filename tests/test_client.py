"""
test ipfs api interface.

"""
import pytest

from .server import (
    VERSION_INFO, NODE_ID

)

pytestmark = pytest.mark.asyncio(forbid_global_loop=True)


async def test_version(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.version()
        assert content == VERSION_INFO

async def test_id(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.id()
        assert content == NODE_ID

# TODO: add the test
# async def test_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.ls()
#         assert content == {}
#

