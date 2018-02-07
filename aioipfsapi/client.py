"""
IPFS client with asyncio

This module wraps the synchrous ipfs api to asynchrous api.

"""
import asyncio
import aiohttp
import logging

from aiohttp import client_exceptions
from ipfsapi import (
    Client, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_BASE, assert_version
)
from ipfsapi.http import HTTPClient
from ipfsapi.multipart import default_chunk_size

__all__ = ['AioClient', 'connect']

logger = logging.getLogger(__name__)


async def connect(host=DEFAULT_HOST, port=DEFAULT_PORT, base=DEFAULT_BASE,
                  loop=None, chunk_size=default_chunk_size, **defaults):
    # Create client instance
    client = AioClient(host, port, base, chunk_size, loop, **defaults)

    # Query version number from daemon and validate it
    resp = await client.version()

    assert_version(resp['Version'])

    return client


class AioHttpClient(HTTPClient):
    """
    An aio http client for interacting with IPFS deamon

    """

    def __init__(self, host, port, base, loop, **defaults):
        super().__init__(host, port, base, **defaults)
        self._loop = loop

        self._session = self.session()

    async def _do_request(self, method, *args, **kwargs):
        try:
            async with aiohttp.ClientSession() as sess:
                async with getattr(sess, method)(*args, **kwargs) as resp:
                    resp.raise_for_status()
                    return await resp.read()
        except asyncio.CancelledError:
            raise
        except client_exceptions.ClientError as error:
            raise
        except Exception as error:
            logger.error('Unexpected error', exc_info=True)

            raise

    async def _request(self, method, url, params, parser, stream=False,
                       files=None, headers={}, data=None):
        # TODO: allows files and stream
        resp = await self._do_request(method, url=url, params=params,
                                      headers=headers, data=data)

        if stream:
            # Raise exceptions for response status
            self._do_raise_for_status(resp)

            # Decode each item as it is read
            def stream_decode():
                for data in resp:
                    for result in parser.parse_partial(data):
                        yield result
                for result in parser.parse_finalize():
                    yield result
            return stream_decode()
        else:
            # First decode received item
            ret = parser.parse(resp)

            return ret


class AioClient(Client):

    _clientfactory = AioHttpClient

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT,
                 base=DEFAULT_BASE, chunk_size=default_chunk_size,
                 loop=None, **defaults):
        """Connects to the API port of an IPFS node."""

        self.chunk_size = chunk_size

        self._loop = loop or asyncio.get_event_loop()

        self._client = self._clientfactory(host, port, base, loop, **defaults)
