# encoding: utf-8
import sys
import os

import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi._utils import base_url
from riotApi import Client


championmastery = Client(test_api_key, unlimited=True).championmastery


class TestChampionMaster(BaseTestClass):
    control_url = '{}/championmastery/location/EUN1/player/1/champion/1'.format(base_url)

    @pytest.fixture
    def data(self):
        return championmastery.champion_master(1, 1)


class TestChampionPoints(BaseTestClass):
    control_url = '{}/championmastery/location/EUN1/player/6/champions'.format(base_url)

    @pytest.fixture
    def data(self):
        return championmastery.champions_points(6)


class TestScore(BaseTestClass):
    control_url = '{}/championmastery/location/EUN1/player/2/score'.format(base_url)

    @pytest.fixture
    def data(self):
        return championmastery.score(2)


class TestTopChampions(BaseTestClass):
    control_url = '{}/championmastery/location/EUN1/player/2/topchampions'.format(base_url)

    @pytest.fixture
    def data(self):
        return championmastery.top_champions(2, count=3)

    def test_params(self, data):
        assert self.request_params['count'] == 3
