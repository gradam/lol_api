# encoding: utf-8
import multiprocessing
from time import sleep

import pytest
import requests

from lol_api._daemon import ApiDaemon
from lol_api._utils import count_request
from lol_api.exceptions import RateLimitExceededError

daemon = ApiDaemon(log=False)
t = multiprocessing.Process(target=daemon.run)


class TestDaemon:
    message = 'test'
    server = ('localhost', 8877)
    api_key = 'testkey'

    @classmethod
    def setup_class(cls):
        t.start()
        sleep(0.05)

    @count_request
    def api_func(self, region=None):
        return self.message

    def test_short_request_unavailable(self):
        with pytest.raises(RateLimitExceededError):
            for _ in range(11):
                self.api_func(region='euw')

    def test_short(self):
        for _ in range(9):
            self.api_func(region='eune')

    def test_different_api_key(self):
        for _ in range(10):
            self.api_func(region='las')

        self.api_key = 'testkey2'

        for _ in range(10):
            self.api_func(region='las')

    @classmethod
    def teardown_class(cls):
        t.terminate()
