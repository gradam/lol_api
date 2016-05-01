# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi import Client
from riotApi._utils import base_url

game = Client(test_api_key, unlimited=True).Game


class TestRecent(BaseTestClass):
    control_url = '{}/api/lol/eune/v1.3/game/by-summoner/123/recent'.format(base_url)

    @pytest.fixture
    def data(self):
        return game.recent(123)
