# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import region_default, api_versions
from riotApi._utils import base_url
from utils import test_api_key, BaseTestClass

game = Client(test_api_key, unlimited=True).Game

version = api_versions['game']
api_url = '{}/api/lol/{}/{}/game/'.format(base_url, region_default, version)


class TestRecent(BaseTestClass):
    control_url = '{}by-summoner/123/recent'.format(api_url)

    @pytest.fixture
    def data(self):
        return game.recent(123)
