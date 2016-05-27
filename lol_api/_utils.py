# encoding: utf-8

import os
import time
import json
import socket
from collections import namedtuple, deque

import requests

from lol_api.data import error_codes, regions
from lol_api.exceptions import RateLimitExceededError, InvalidRegionError

base_url = 'https://{}.api.pvp.net'


def check_response_code(response_code, url):
    if response_code != 200:
        error_massage = 'Error code: {} - {}\nurl={}'.format(response_code,
                                                             error_codes[response_code], url)
        raise requests.RequestException(error_massage)


def send_request(api_key, region, server):
    data = json.dumps({
        'api_key': api_key,
        'region': region
    })
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(server)
    sock.sendall(bytes(data, 'utf-8'))

    received_data = sock.recv(1024).decode('utf-8')
    response = json.loads(received_data)['available']

    return response


def count_request(func):
    def wrapper(self, *args, **kwargs):
        try:
            region = kwargs['region']
            region_validation(region)
        except KeyError:
            region = self.region_default

        if self.server:
            is_available = send_request(self.api_key, region, self.server)
        else:
            if self.watcher.request_available(region):
                is_available = True
                self.watcher.add_request(region)
            else:
                is_available = False

        if is_available:
            return func(self, *args, **kwargs)
        else:
            raise RateLimitExceededError

    return wrapper


def get_champion_id(value):
    try:
        value = int(value)
        return value
    except ValueError:
        raise NotImplementedError
        # TODO: get champion ID from name


def to_comma_separated(ids):
    if isinstance(ids, str):
        return ids
    elif isinstance(ids, int):
        return str(ids)
    else:
        return ','.join([str(x) for x in ids])


def region_validation(region):
    region = region.lower()
    try:
        return regions[region]
    except KeyError:
        if region in regions.values():
            return region
    raise InvalidRegionError


class RateLimitWatcher:
    def __init__(self, production=False, unlimited=False):
        self.long_limit_time = 600
        self.short_limit_time = 10
        self.unlimited = unlimited
        Limit = namedtuple('Limits', ['requests', 'seconds'])
        if production:
            self.short_limit = Limit(requests=3000, seconds=self.short_limit_time)
            self.long_limit = Limit(requests=180000, seconds=self.long_limit_time)
        else:
            self.short_limit = Limit(requests=10, seconds=self.short_limit_time)
            self.long_limit = Limit(requests=500, seconds=self.long_limit_time)
        self.made_requests = {
            region: deque(maxlen=self.long_limit.requests) for region in regions.values()
            }

    def add_request(self, region):
        self.made_requests[region].append(time.time())

    def _reload(self, region):
        t = time.time() - self.long_limit_time
        while len(self.made_requests[region]) > 0 and self.made_requests[region][0] < t:
            self.made_requests[region].popleft()

    def request_available(self, region):
        self._reload(region)

        if self.unlimited:
            return True

        requests_limit = self.long_limit.requests
        request_number = len(self.made_requests[region])
        if self._short_limit_not_exceeded(region) and request_number != requests_limit:
            return True
        else:
            return False

    def _short_limit_not_exceeded(self, region):
        try:
            earliest_short_requests = self.made_requests[region][self.short_limit.requests - 1]
        except IndexError:
            earliest_short_requests = time.time() - 30

        return earliest_short_requests < time.time() - self.short_limit_time