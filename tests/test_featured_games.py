# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi import Client


featured_games = Client(test_api_key, unlimited=True).FeaturedGames


class Test(BaseTestClass):
    control_url = 'https://eune.api.pvp.net/observer-mode/rest/featured'

    @pytest.fixture
    def data(self):
        return featured_games.featured()
