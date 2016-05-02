# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import api_versions
from riotApi._utils import base_url
from tests.utils import BaseTestClass, test_api_key


champion_api = Client(test_api_key, unlimited=True).Champion
api_url = '{}/api/lol/eune/{}'.format(base_url, api_versions['champion'])


class TestChampionsAll(BaseTestClass):
    control_url = '{}/champion'.format(api_url)

    @pytest.fixture
    def data(self):
        return champion_api.champions_all()


class TestChampion(BaseTestClass):
    control_url = '{}/champion/1'.format(api_url)

    @pytest.fixture
    def data(self):
        return champion_api.champion(champion_id=1)
