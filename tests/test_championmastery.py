# encoding: utf-8
import pytest

from lol_api.api.championmastery import *
from lol_api.data import platforms
from lol_api._utils import base_url

from tests.utils import BaseTestClass, initialize_settings, region_default


platform = platforms[region_default]
api_url = '{}/championmastery/location/{}/player/'.format(base_url, platform)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()


class TestChampionMaster(BaseTestClass):
    control_url = '{}1/champion/1'.format(api_url)

    @pytest.fixture
    def data(self):
        return champion_master(1, 1)


class TestChampionPoints(BaseTestClass):
    control_url = '{}6/champions'.format(api_url)

    @pytest.fixture
    def data(self):
        return champions_points(6)


class TestScore(BaseTestClass):
    control_url = '{}2/score'.format(api_url)

    @pytest.fixture
    def data(self):
        return score(2)


class TestTopChampions(BaseTestClass):
    control_url = '{}2/topchampions'.format(api_url)

    @pytest.fixture
    def data(self):
        return top_champions(2, count=3)

    def test_params(self, data):
        assert self.request_params['count'] == 3
