import os
import six

default_chunk_size = 4096

def stream_filesystem_node(path,
                           recursive=False,
                           patterns='**'):
    """Gets a buffered generator for streaming either files or directories.

    Returns a buffered generator which encodes the file or directory at the
    given path as :mimetype:`multipart/form-data` with the corresponding
    headers.
    
    """
    is_dir = isinstance(path, six.string_types) and os.path.isdir(path)
    if recursive or is_dir:
        pass
        # return stream_directory(path, recursive, patterns, chunk_size)
    else:
        return {'files': open(path, 'rb')}