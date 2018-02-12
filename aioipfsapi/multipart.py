import os
import six
from pathlib import Path
from aiohttp import FormData


default_chunk_size = 4096


def stream_files(path, data):
    """
    Get multipart data explicitly
    :param path: (PurePath) path obj
    :param data: (FormData) multipart/form-data stream obj
    :return: data
    """
    data.add_field('file', open(str(path), 'rb'), filename=path.name)
    return data


def stream_directory(path, recursive, patterns):
    pass


def stream_filesystem_node(path,
                           recursive=False,
                           patterns='**'):
    """Gets a buffered generator for streaming either files or directories.

    Returns a buffered generator which encodes the file or directory at the
    given path as :mimetype:`multipart/form-data` with the corresponding
    headers.

    """
    is_dir = isinstance(path, six.string_types) and os.path.isdir(path)
    data = FormData()
    path = Path(path)
    if recursive or is_dir:
        pass
        return stream_directory(path, data, patterns)
    else:
        return stream_files(path, data)



