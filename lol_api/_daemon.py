# encoding: utf-8

import json
import socketserver
from functools import partial

from lol_api._utils import RateLimitWatcher


class RequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, api_keys, production, unlimited, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.api_keys = api_keys
        self.production = production
        self.unlimited = unlimited

    def is_request_available(self, api_key, region):
        try:
            watcher = self.api_keys[api_key]
        except KeyError:
            watcher = RateLimitWatcher(self.production, self.unlimited)
            self.api_keys[api_key] = watcher
        if watcher.request_available(region):
            watcher.add_request(region)
            return True
        else:
            return False

    def handle(self):
        data = self.request.recv(1024).strip()
        data = str(data)
        data = json.loads(data)

        api_key = data['api_key']
        region = data['region']

        request_available = self.is_request_available(api_key, region)
        response_data = {'available': request_available}
        response_data = json.dumps(response_data)

        self.request.sendall(response_data)


class ApiDaemon:
    def __init__(self, port=8877, production=False, unlimited=False):
        self.api_keys = {}
        self.port = port
        self.host = 'localhost'
        self.production = production
        self.unlimited = unlimited

    def run(self):
        Handler = partial(RequestHandler, self.api_keys, self.production, self.unlimited)
        server = socketserver.ThreadingTCPServer((self.host, self.port), Handler)

        server.serve_forever()


