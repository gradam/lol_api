# encoding: utf-8

import json
from time import gmtime, strftime
from functools import partial

import socketserver

from lol_api._utils import RateLimitWatcher


class RequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, api_keys, production, unlimited, logging, *args, **kwargs):
        self.api_keys = api_keys
        self.production = production
        self.unlimited = unlimited
        self.logging = logging

        super().__init__(*args, **kwargs)

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

    def log(self, request_available, request_information):
        if self.logging:
            t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            log = '{}  |  {}  |  {}  |  response: {}'.format(t, self.client_address,
                                                             request_information, request_available)
            print(log)

    def handle(self):
        data = self.request.recv(1024).strip()
        data = data.decode('utf-8')
        data = json.loads(data)

        api_key = data['api_key']
        region = data['region']

        request_available = self.is_request_available(api_key, region)
        response_data = {'available': request_available}
        response_data = bytes(json.dumps(response_data), 'utf-8')

        self.log(request_available, (api_key, region))

        self.request.sendall(response_data)


class ApiDaemon:
    def __init__(self, port=8877, host='localhost', production=False, unlimited=False, log=True):
        self.api_keys = {}
        self.port = port
        self.host = host
        self.production = production
        self.unlimited = unlimited
        self.log = log

    def run(self):
        Handler = partial(RequestHandler, self.api_keys, self.production, self.unlimited, self.log)
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        server = socketserver.ThreadingTCPServer((self.host, self.port), Handler)
        server.serve_forever()


