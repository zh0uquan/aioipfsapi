import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as sess:
        async with sess.get(
            url='http://localhost:5001/api/v0/version',
            params=[('stream-channels', 'false'),
                    ('arg', 'QmTkzDwWqPbnAh5YiV5VwcTLnGdwSNsNTn2aDxdXBFca7D')]
        ) as resp:
            print(await resp.json())
            return resp

loop = asyncio.get_event_loop()

loop.run_until_complete(main())
