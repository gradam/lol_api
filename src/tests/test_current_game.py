# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import region_default, platforms
from riotApi._utils import base_url
from tests.utils import test_api_key, BaseTestClass

platform = platforms[region_default]
current_game = Client(test_api_key, unlimited=True).CurrentGame


class TestSpectatorGameInfo(BaseTestClass):
    control_url = '{}/observer-mode/rest/consumer/getSpectatorGameInfo/EUN1/123'.format(base_url,
                                                                                        platform)

    @pytest.fixture
    def data(self):
        return current_game.spectator_game_info(123)
