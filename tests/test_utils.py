from time import time

import pytest
import requests

from lol_api._utils import check_response_code, RateLimitWatcher, count_request, get_champion_id, \
    region_validation
from lol_api.exceptions import RateLimitExceededError, InvalidRegionError
from lol_api.data import regions


def test_check_response_code():
    check_response_code(200)


def test_bad_response_code():
    with pytest.raises(requests.RequestException):
        check_response_code(500)


class TestRateLimitWatcher:

    @pytest.fixture
    def watcher(self):
        return RateLimitWatcher(production=False)

    def test_add_request(self, watcher):
        watcher.add_request('eune')
        assert len(watcher.made_requests['eune']) == 1

    def test_reload(self, watcher):
        watcher.made_requests['euw'].append(time() - 601)
        watcher.made_requests['euw'].append(time() - 599)
        watcher._reload('euw')
        assert len(watcher.made_requests['euw']) == 1

    def test_request_available(self, watcher):
        assert watcher.request_available('eune') is True

    def test_request_unavailable(self, watcher):
        for _ in range(500):
            watcher.add_request('euw')
        assert watcher.request_available('euw') is False

    def test_short_request_unavailable(self, watcher):
        for _ in range(10):
            watcher.add_request('eune')
        assert watcher.request_available('eune') is False

    def test_production(self):
        watcher = RateLimitWatcher(production=True)
        for _ in range(40):
            watcher.add_request('eune')
        assert watcher.request_available('eune') is True


class TestCountRequest:
    message = 'test'

    @count_request
    def api_func(self, region=None):
        return self.message

    @pytest.fixture(autouse=True)
    def set_watcher(self):
        self.watcher = RateLimitWatcher(production=False)

    def test_return(self):
        assert self.api_func(region='eune') == self.message

    def test_counter(self):
        self.api_func(region='euw')
        self.api_func(region='euw')
        assert len(self.watcher.made_requests['euw']) == 2

    def test_rate_limit_exceeded_error_rise(self):
        for _ in range(10):
            self.api_func(region='eune')
        with pytest.raises(RateLimitExceededError):
            self.api_func(region='eune')
        assert self.watcher.request_available('euw') is True


def test_get_champion_id():
    assert get_champion_id(5) == 5

    with pytest.raises(NotImplementedError):
        get_champion_id('annie')


def test_region_validation():
    assert region_validation('brazil') == regions['brazil']
    assert region_validation(regions['brazil']) == regions['brazil']


def test_region_validation_invalid_region():
    with pytest.raises(InvalidRegionError):
        region_validation('not_valid')
