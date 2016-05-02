# encoding: utf-8

import os
import time
from collections import deque, namedtuple

import requests

from riotApi.data import error_codes
from riotApi.exceptions import RateLimitExceededError


directory = os.path.dirname(os.path.realpath(__file__))
base_url = 'https://global.api.pvp.net'


class RateLimitWatcher:
    def __init__(self, production=False, unlimited=False):
        self.unlimited = unlimited
        Limit = namedtuple('Limits', ['requests', 'seconds'])
        if production:
            self.short_limit = Limit(requests=3000, seconds=10)
            self.long_limit = Limit(requests=180000, seconds=600)
        else:
            self.short_limit = Limit(requests=10, seconds=10)
            self.long_limit = Limit(requests=500, seconds=600)
        self.made_requests = deque(maxlen=self.long_limit.requests)

    def add_request(self):
        self.made_requests.append(time.time())

    def _reload(self):
        t = time.time() - 600
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def request_available(self):
        self._reload()
        if self.unlimited:
            return True
        try:
            latest_short_requests = self.made_requests[self.short_limit.requests - 1]
        except IndexError:
            latest_short_requests = time.time() - 30
        requests_limit = self.long_limit.requests
        if latest_short_requests < time.time() - 10 and len(self.made_requests) != requests_limit:
            return True
        else:
            return False


def check_response_code(response_code):
    if response_code != 200:
        error_massage = 'Error code: {} - {}'.format(response_code, error_codes[response_code])
        raise requests.RequestException(error_massage)


def count_request(func):
    def wrapper(self, *args, **kwargs):
        if self.watcher.request_available():
            self.watcher.add_request()
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


