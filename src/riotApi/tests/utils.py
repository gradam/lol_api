import json

import pytest
import requests


class MockRequest:
    def __init__(self, json_data, code=200):
        self.json_data = json_data
        self.status_code = code

    def json(self):
        return json.dumps(self.json_data)


@pytest.fixture(autouse=True)
def mock_request_get(monkeypatch):
    monkeypatch.setattr(requests, 'get', _mock_request)


def _mock_request(*args, **kwargs):
    return MockRequest('some_data')
