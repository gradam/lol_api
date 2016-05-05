# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import api_versions
from riotApi._utils import base_url
from utils import test_api_key, BaseTestClass


region_default = 'euw'
stats = Client(test_api_key, region_default, unlimited=True).Stats

version = api_versions['stats']
api_url = '{}/api/lol/{}/{}/stats/'.format(base_url, region_default, version)


class TestRanked(BaseTestClass):
    control_url = '{}by-summoner/123/ranked'.format(api_url)

    @pytest.fixture
    def data(self):
        return stats.ranked(123)


class TestSummary(BaseTestClass):
    control_url = '{}by-summoner/123/summary'.format(api_url)

    @pytest.fixture
    def data(self):
        return stats.summary(123)
