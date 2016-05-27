# encoding: utf-8
import pytest

from lol_api.client import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass


region_default = 'eune'
matchlist = Client(test_api_key, region_default, unlimited=True).Matchlist


version = api_versions['matchlist']
api_url = '{}/api/lol/{}/{}/matchlist/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


class TestBySummoner(BaseTestClass):
    control_url = '{}by-summoner/123'.format(api_url)

    @pytest.fixture
    def data(self):
        return matchlist.by_summoner(123)
