"""
Preset IPFS Server

"""
import multiprocessing

class IPFSServer(object):

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self._process = None

    def start(self):
        def worker(app, port):
            # TODO here we create a dummy flask server to emulate the
            # ipfs server api
            pass

        self._process = multiprocessing.Process(
            target=worker,
            args=(self.app, self.port)
        )
        self._process.start()

    def stop(self):
        if self._process:
            self._process.terminate()




