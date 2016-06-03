# encoding: utf-8
import pytest

from lol_api.api.current_game import *
from lol_api.data import platforms
from lol_api.utils import base_url
from tests.utils import region_default, initialize_settings, BaseTestClass

platform = platforms[region_default]


def setup_module(module):
    initialize_settings()


class TestSpectatorGameInfo(BaseTestClass):
    control_url = '{}/observer-mode/rest/consumer/getSpectatorGameInfo/EUN1/123'.format(base_url,
                                                                                        platform)
    control_url = control_url.format(region_default)

    @pytest.fixture
    def data(self):
        return spectator_game_info(123)
