import pytest
import requests

from lol_api.settings import settings

test_api_key = 'test_key'

region_default = 'eune'


class BaseTestClass:
    control_url = ''
    test_json = {"3": "bb", "a": 4}

    #
    request_params = {}
    mock_request = None  # Will be MockRequest object
    requested_url = ''

    @pytest.fixture(autouse=True)
    def mock_request_get(self, monkeypatch):
        monkeypatch.setattr(requests, 'get', self.get_mock_func)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.request_params = {}
        self.mock_request = MockRequest(self.test_json)

    def get_mock_func(self, url, **kwargs):
        self.requested_url = url
        self.request_params = (kwargs['params'])
        return self.mock_request

    def test_api_key(self, data):
        assert self.request_params['api_key'] == test_api_key

    def test_response_data(self, data):
        assert data == self.test_json

    def test_requested_url(self, data):
        assert self.requested_url == self.control_url


class MockRequest:
    def __init__(self, json_data, code=200):
        self.json_data = json_data
        self.status_code = code

    def json(self):
        return self.json_data


@pytest.fixture(autouse=True)
def mock_request_get(monkeypatch):
    monkeypatch.setattr(requests, 'get', _mock_request)


def _mock_request(*args, **kwargs):
    return MockRequest('some_data')


def initialize_settings():
    settings.API_KEY = test_api_key
    settings.REGION_DEFAULT = region_default
    settings.initialize_watcher(unlimited=True)

