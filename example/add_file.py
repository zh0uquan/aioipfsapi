"""
This example shows how to add a text file to the local node

"""
import tempfile
import asyncio
import aioipfsapi

async def async_add():
    async with aioipfsapi.AioClient() as api:
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(b'hello world')
            resp = await api.add(files=fp.name)
            print(resp)

async def async_add_files():
    async with aioipfsapi.AioClient() as api:
        with tempfile.TemporaryFile() as fp1, \
                tempfile.NamedTemporaryFile() as fp2:

            fp1.write(b'hello world')
            fp2.write(b'hello world')
            dirname = tempfile.gettempdir()

            resp = await api.add(files=dirname, recursive=True)
            print(resp)

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.gather(*[async_add(), async_add_files()]))
