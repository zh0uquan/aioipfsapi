"""
Preset IPFS Server

"""
from flask import Flask, jsonify
import multiprocessing

app = Flask(__name__)

VERSION = {
  'Version': '0.4.14-dev',
  'Commit': 'b37f856',
  'Repo': '6',
  'System': 'amd64/linux',
  'Golang': 'go1.9.3'
}


@app.route("/api/v0/version")
def version():
    return jsonify(VERSION)


ID = {
  'ID': '12345',
  'PublicKey': 'pkey',
  'Addresses': [
    '/ip4/127.0.0.1/tcp/4001/ipfs/12345',
    '/ip4/172.17.0.1/tcp/4001/ipfs/12345',
    '/ip4/172.18.0.1/tcp/4001/ipfs/12345',
    '/ip4/192.168.126.36/tcp/4001/ipfs/12345',
    '/ip6/::1/tcp/4001/ipfs/12345',
    '/ip4/84.138.93.214/tcp/4001/ipfs/12345'
  ],
  'AgentVersion': 'go-ipfs/0.4.14-dev/b37f856',
  'ProtocolVersion': 'ipfs/0.1.0'
}


@app.route("/api/v0/id")
def id():
    return jsonify(ID)

PEERS = {
  'Peers': [{
    'Addr': '/ip4/104.131.169.41/tcp/4001',
    'Peer': 'QmVGkGSV25o3AMjcjjnPVb1PqJzrA1PvvhMiV57cMEuExb',
    'Latency': '',
    'Muxer': '*sm_yamux.conn',
    'Streams': None
  }, {
    'Addr': '/ip4/99.229.246.68/tcp/36306',
    'Peer': 'QmfMf95tEQhJGGgsCmuHYtDZtWb5RvyeVRWTQXY6mQH5PD',
    'Latency': '',
    'Muxer': '*sm_yamux.conn',
    'Streams': None
  }]
}


@app.route('/api/v0/swarm/peers')
def peers():
    return jsonify(PEERS)


class IPFSServer(object):

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self._process = None

    def start(self):
        def worker(hostname, port):
            app.run(hostname, port)

        self._process = multiprocessing.Process(
            target=worker,
            args=(self.hostname, self.port)
        )
        self._process.start()

    def stop(self):
        if self._process:
            self._process.terminate()



