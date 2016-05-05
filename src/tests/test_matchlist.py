# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import api_versions
from riotApi._utils import base_url
from utils import test_api_key, BaseTestClass


region_default = 'eune'
matchlist = Client(test_api_key, region_default, unlimited=True).Matchlist


version = api_versions['matchlist']
api_url = '{}/api/lol/{}/{}/matchlist/'.format(base_url, region_default, version)


class TestBySummoner(BaseTestClass):
    control_url = '{}by-summoner/123'.format(api_url)

    @pytest.fixture
    def data(self):
        return matchlist.by_summoner(123)
