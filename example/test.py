import asyncio
from aioipfsapi import AioClient

async def task():
    c = AioClient()
    content = await c.id()
    print(content)
    await asyncio.sleep(3)


loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.gather(*[task() for i in range(4)]))
