# encoding: utf-8
import sys
import os

import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import riotApi
from riotApi.lol_static_data import get_every_champions_info


class MockRequest:
    def __init__(self, json, code=200):
        self.json_data = json
        self.status_code = code

    def json(self):
        return self.json_data


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


class TestGetEveryChampionsInfo:

    @pytest.fixture(autouse=True)
    def mock_request_get(self, monkeypatch):
        monkeypatch.setattr(requests, 'get', self.get_mock_func)

    @pytest.fixture(autouse=True)
    def clear_params(self):
        self.request_params = {}

    def get_mock_func(self, url, **kwargs):
        self.request_params = (kwargs['params'])
        return self.mock_request

    def test_get_every_champions_info(self):
        self.mock_request = MockRequest('some data')

        assert get_every_champions_info(champData='all') == 'some data'
        assert self.request_params['api_key'] == riotApi.api_key
        assert self.request_params['champData'] == 'all'

