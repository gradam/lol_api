# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi._utils import base_url, platforms, region_default
from riotApi import Client


championmastery = Client(test_api_key, unlimited=True).Championmastery
platform = platforms[region_default]
api_url = '{}/championmastery/location/{}/player/'.format(base_url, platform)


class TestChampionMaster(BaseTestClass):
    control_url = '{}1/champion/1'.format(api_url)

    @pytest.fixture
    def data(self):
        return championmastery.champion_master(1, 1)


class TestChampionPoints(BaseTestClass):
    control_url = '{}6/champions'.format(api_url)

    @pytest.fixture
    def data(self):
        return championmastery.champions_points(6)


class TestScore(BaseTestClass):
    control_url = '{}2/score'.format(api_url)

    @pytest.fixture
    def data(self):
        return championmastery.score(2)


class TestTopChampions(BaseTestClass):
    control_url = '{}2/topchampions'.format(api_url)

    @pytest.fixture
    def data(self):
        return championmastery.top_champions(2, count=3)

    def test_params(self, data):
        assert self.request_params['count'] == 3
