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
from riotApi._utils import RateLimitWatcher


class Client:
    def __init__(self, api_key, production=False, unlimited=False):
        self.api_key = api_key
        self.watcher = RateLimitWatcher(production, unlimited=unlimited)

        self.LolStaticData = LolStaticData(api_key=self.api_key)
        self.LocalData = LocalData(self.LolStaticData)
        self.LolStatus = LolStatus()

        self.Championmastery = ChampionMastery(api_key=self.api_key, watcher=self.watcher)
        self.Champion = Champion(api_key=self.api_key, watcher=self.watcher)
        self.CurrentGame = CurrentGame(api_key=self.api_key, watcher=self.watcher)
        self.FeaturedGames = FeaturedGames(api_key=self.api_key, watcher=self.watcher)
        self.Game = Game(api_key=self.api_key, watcher=self.watcher)
        self.League = League(api_key=self.api_key, watcher=self.watcher)
        self.Match = Match(api_key=self.api_key, watcher=self.watcher)
        self.Matchlist = Matchlist(api_key=self.api_key, watcher=self.watcher)
        self.Stats = Stats(api_key=self.api_key, watcher=self.watcher)
        self.Summoner = Summoner(api_key=self.api_key, watcher=self.watcher)
        self.Team = Team(api_key=self.api_key, watcher=self.watcher)
