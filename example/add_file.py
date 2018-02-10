"""
This example shows how to add a text file to the local node

"""
import os
import asyncio
import aioipfsapi

async def async_add():
    async with aioipfsapi.AioClient() as api:
        try:
            filename = 'tmpfile'
            with open(filename, 'w') as fp:
                fp.write('hello world')
                resp = await api.add(files=filename)
        except Exception as err:
            raise err
        finally:
            os.remove(filename)

loop = asyncio.get_event_loop()

loop.run_until_complete(async_add())
