# encoding: utf-8
import pytest

from lol_api.client import Client
from tests.utils import test_api_key, BaseTestClass

region_default = 'euw'

featured_games = Client(test_api_key, region_default, unlimited=True).FeaturedGames


class TestFeaturedGames(BaseTestClass):
    control_url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region_default)

    @pytest.fixture
    def data(self):
        return featured_games.featured()
