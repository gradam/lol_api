# encoding: utf-8
import os

from lol_api.api._champion import Champion
from lol_api.api._championmastery import ChampionMastery
from lol_api.api._current_game import CurrentGame
from lol_api.api._featured_games import FeaturedGames
from lol_api.api._game import Game
from lol_api.api._league import League
from lol_api.api._lol_status import LolStatus
from lol_api.api._match import Match
from lol_api.api._matchlist import Matchlist
from lol_api.api._stats import Stats
from lol_api.api._summoner import Summoner
from lol_api.api._team import Team

from lol_api.api._lol_static_data import LolStaticData
from lol_api.db import LocalData
from lol_api._utils import RateLimitWatcher
from lol_api._utils import region_validation

from lol_api.exceptions import NoApiKeySpecified, RegionDefaultNotSpecified
from lol_api.settings import settings


class Client:
    def __init__(self, api_key=None, region_default=None, production=False, unlimited=False,
                 server=()):
        self.api_key = self.get_api_key(api_key)
        self.server = server
        self.region_default = self.get_region_default(region_default)
        self.watcher = RateLimitWatcher(production, unlimited=unlimited)

        self.LolStaticData = LolStaticData(api_key=self.api_key, region_default=self.region_default)
        self.LocalData = LocalData(self.LolStaticData)
        self.LolStatus = LolStatus(region_default=self.region_default)

        parameters = {'api_key': self.api_key,
                      'watcher': self.watcher,
                      'region_default': self.region_default,
                      'server': self.server}

        self.Championmastery = ChampionMastery(**parameters)
        self.Champion = Champion(**parameters)
        self.CurrentGame = CurrentGame(**parameters)
        self.FeaturedGames = FeaturedGames(**parameters)
        self.Game = Game(**parameters)
        self.League = League(**parameters)
        self.Match = Match(**parameters)
        self.Matchlist = Matchlist(**parameters)
        self.Stats = Stats(**parameters)
        self.Summoner = Summoner(**parameters)
        self.Team = Team(**parameters)

    @staticmethod
    def get_api_key(api_key):
        if not (api_key or settings.API_KEY):
            try:
                return os.environ['LOL_API_KEY']
            except KeyError:
                raise NoApiKeySpecified

        return api_key if api_key else settings.API_KEY

    @staticmethod
    def get_region_default(region_default):
        if region_default:
            return region_validation(region_default)
        elif settings.REGION_DEFAULT:
            return settings.REGION_DEFAULT
        else:
            raise RegionDefaultNotSpecified

