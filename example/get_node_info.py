"""
This example shows how to get the local node id and one of ipfs default block

"""

import asyncio

import aioipfsapi

async def async_id():
    api = await aioipfsapi.connect()
    content = await api.id()
    print(content)
    await asyncio.sleep(1)

async def async_ls():
    async with aioipfsapi.AioClient() as api:
        content = await api.ls('QmTkzDwWqPbnAh5YiV5VwcTLnGdwSNsNTn2aDxdXBFca7D')
        print('content: {}'.format(content))

loop = asyncio.get_event_loop()

tasks = [async_id() for i in range(3)]
tasks.append(async_ls())

loop.run_until_complete(asyncio.gather(*tasks))

