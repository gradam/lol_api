# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import region_default, api_versions
from riotApi._utils import base_url
from utils import test_api_key, BaseTestClass

match = Client(test_api_key, unlimited=True).Match

version = api_versions['match']
api_url = '{}/api/lol/{}/{}/match/'.format(base_url, region_default, version)


class TestMatch(BaseTestClass):
    control_url = '{}123'.format(api_url)

    @pytest.fixture
    def data(self):
        return match.match(123)
