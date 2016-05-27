# encoding: utf-8
import pytest

from lol_api.api.featured_games import *
from tests.utils import region_default, initialize_settings, BaseTestClass


def setup_module(module):
    initialize_settings()


class TestFeaturedGames(BaseTestClass):
    control_url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region_default)

    @pytest.fixture
    def data(self):
        return featured()
