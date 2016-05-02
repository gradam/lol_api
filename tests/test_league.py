# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi import Client
from riotApi._utils import base_url

league = Client(test_api_key, unlimited=True).League


class TestBySummoner(BaseTestClass):
    control_url = '{}/api/lol/eune/v2.5/league/by-summoner/123,111'.format(base_url)

    @pytest.fixture
    def data(self):
        return league.by_summoners([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/eune/v2.5/league/by-summoner/123,222'.format(base_url)
        league.by_summoners('123,222')
        assert self.requested_url == test_url
