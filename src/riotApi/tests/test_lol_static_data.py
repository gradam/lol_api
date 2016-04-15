# encoding: utf-8
import sys
import os

import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi import api_key, base_url
from riotApi.lol_static_data import every_champions_info, champion_info


class MockRequest:
    def __init__(self, json, code=200):
        self.json_data = json
        self.status_code = code

    def json(self):
        return self.json_data


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


class BaseTestClass:
    control_url = ''

    @pytest.fixture(autouse=True)
    def mock_request_get(self, monkeypatch):
        monkeypatch.setattr(requests, 'get', self.get_mock_func)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.request_params = {}
        self.mock_request = MockRequest('some data')

    def get_mock_func(self, url, **kwargs):
        self.requested_url = url
        self.request_params = (kwargs['params'])
        return self.mock_request

    def test_api_key(self, data):
        assert self.request_params['api_key'] == api_key

    def test_response_data(self, data):
        assert data == 'some data'

    def test_requested_url(self, data):
        assert self.requested_url == self.control_url


class TestGetEveryChampionsInfo(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/champion'.format(base_url)

    @pytest.fixture()
    def data(self):
        return every_champions_info(champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'


class TestGetChampionInfo(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/champion/1'.format(base_url)

    @pytest.fixture()
    def data(self):
        return champion_info(champ_id=1, champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'

# class TestItemsInfo(BaseTestClass)
