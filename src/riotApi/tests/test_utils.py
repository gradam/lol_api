import sys
import os
from time import time

import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi._utils import check_response_code, RateLimitWatcher, count_request
from riotApi.exceptions import RateLimitExceededError


def test_check_response_code():
    check_response_code(200)


def test_bad_response_code():
    with pytest.raises(requests.RequestException):
        check_response_code(500)


class TestRateLimitWatcher:

    @staticmethod
    @pytest.fixture
    def watcher():
        return RateLimitWatcher(production=False)

    @staticmethod
    def test_add_request(watcher):
        watcher.add_request()
        assert len(watcher.made_requests) == 1

    @staticmethod
    def test_reload(watcher):
        watcher.made_requests.append(time() - 900)
        watcher.made_requests.append(time())
        watcher._reload()
        assert len(watcher.made_requests) == 1

    @staticmethod
    def test_request_available(watcher):
        assert watcher.request_available() is True

    @staticmethod
    def test_request_unavailable(watcher):
        for _ in range(500):
            watcher.add_request()
        assert watcher.request_available() is False


class TestCountRequest:
    message = 'test'

    watcher = RateLimitWatcher(production=False)

    @count_request
    def api_func(self):
        return self.message

    @pytest.fixture(autouse=True)
    def set_watcher(self):
        self.watcher = RateLimitWatcher(production=False)

    def test_return(self):
        assert self.api_func() == self.message

    def test_counter(self):
        self.api_func()
        self.api_func()
        assert len(self.watcher.made_requests) == 2

    def test_rate_limit_exceeded_error_rise(self):
        for _ in range(10):
            self.api_func()
        with pytest.raises(RateLimitExceededError):
            self.api_func()
