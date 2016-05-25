# encoding: utf-8
import pytest

from lol_api import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass


region_default = 'euw'
stats = Client(test_api_key, region_default, unlimited=True).Stats

version = api_versions['stats']
api_url = '{}/api/lol/{}/{}/stats/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


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
