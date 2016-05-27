# encoding: utf-8
import time
from collections import namedtuple, deque

from lol_api.data import regions


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