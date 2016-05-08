# encoding: utf-8
import pytest

from lol_api import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from utils import test_api_key, BaseTestClass

region_default = 'las'
game = Client(test_api_key, region_default, unlimited=True).Game

version = api_versions['game']
api_url = '{}/api/lol/{}/{}/game/'.format(base_url, region_default, version)


class TestRecent(BaseTestClass):
    control_url = '{}by-summoner/123/recent'.format(api_url)

    @pytest.fixture
    def data(self):
        return game.recent(123)
