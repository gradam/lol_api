# encoding: utf-8
import pytest

from lol_api import Client
from lol_api.data import platforms
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass

region_default = 'eune'

platform = platforms[region_default]
current_game = Client(test_api_key, region_default, unlimited=True).CurrentGame


class TestSpectatorGameInfo(BaseTestClass):
    control_url = '{}/observer-mode/rest/consumer/getSpectatorGameInfo/EUN1/123'.format(base_url,
                                                                                        platform)

    @pytest.fixture
    def data(self):
        return current_game.spectator_game_info(123)
