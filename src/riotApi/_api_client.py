# encoding: utf-8
from riotApi._champion import Champion
from riotApi._championmastery import ChampionMastery
from riotApi._current_game import CurrentGame
from riotApi._featured_games import FeaturedGames
from riotApi._game import Game
from riotApi._league import League
from riotApi._local_data import LocalData
from riotApi._lol_static_data import LolStaticData
from riotApi._lol_status import LolStatus
from riotApi._match import Match
from riotApi._matchlist import Matchlist
from riotApi._stats import Stats
from riotApi._summoner import Summoner
from riotApi._team import Team
from riotApi._utils import RateLimitWatcher, region_validation


class Client:
    def __init__(self, api_key, region_default, production=False, unlimited=False):
        self.api_key = api_key
        self.region_default = region_validation(region_default)
        self.watcher = RateLimitWatcher(production, unlimited=unlimited)

        self.LolStaticData = LolStaticData(api_key=self.api_key, region_default=self.region_default)
        self.LocalData = LocalData(self.LolStaticData)
        self.LolStatus = LolStatus(region_default=self.region_default)

        parameters = {'api_key': self.api_key,
                      'watcher': self.watcher,
                      'region_default': self.region_default}

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

