"""
IPFS client with asyncio

This module wraps the synchrous ipfs api to asynchrous api.

"""
import aiohttp
import asyncio
import contextlib
import tarfile

import requests
from six.moves import http_client

from ipfsapi import multipart, encoding
from ipfsapi.http import HTTPClient
from ipfsapi.client import (
    Client, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_BASE)

__all__ = ['AioClient']


class AioHttpClient(HTTPClient):
    """
    An aio http client for interacting with IPFS deamon

    """

    def __init__(self, host, port, base, loop, **defaults):
        super().__init__(host, port, base, **defaults)
        self._loop = loop

    async def _do_request(self, method, *args, **kwargs):
        try:
            if self._session:
                return await getattr(self._session, method)(*args, **kwargs)
            else:
                async with aiohttp.ClientSession() as sess:
                    resp = await getattr(sess, method)(*args, **kwargs)
            return resp
        except requests.ConnectionError as error:
            six.raise_from(exceptions.ConnectionError(error), error)
        except http_client.HTTPException as error:
            six.raise_from(exceptions.ProtocolError(error), error)
        except requests.Timeout as error:
            six.raise_from(exceptions.TimeoutError(error), error)

    async def _request(self, method, url, params, parser, stream=False,
                       files=None, headers={}, data=None):
        # TODO: allows files and stream
        resp = await self._do_request(method, url, params=params, headers=headers, data=data)

        if stream:
            # Raise exceptions for response status
            self._do_raise_for_status(res)

            # Decode each item as it is read
            def stream_decode():
                for data in res:
                    for result in parser.parse_partial(data):
                        yield result
                for result in parser.parse_finalize():
                    yield result
            return stream_decode()
        else:
            # First decode received item
            ret = parser.parse(await resp.read())

            # Raise exception for response status
            # (optionally incorpating the response message, if applicable)

            self._do_raise_for_status(resp, ret)

            resp.close()

            return ret

    def _do_raise_for_status(self, response, content=None):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            # If we have decoded an error response from the server,
            # use that as the exception message; otherwise, just pass
            # the exception on to the caller.
            if isinstance(content, dict) and 'Message' in content:
                msg = content['Message']
                six.raise_from(exceptions.ErrorResponse(msg, error), error)
            else:
                six.raise_from(exceptions.StatusError(error), error)


class AioClient(Client):

    _clientfactory = AioHttpClient

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT,
                 base=DEFAULT_BASE, chunk_size=multipart.default_chunk_size,
                 loop=None, **defaults):
        """Connects to the API port of an IPFS node."""

        self.chunk_size = chunk_size

        self._loop = loop or asyncio.get_event_loop()

        self._client = self._clientfactory(host, port, base, loop, **defaults)
