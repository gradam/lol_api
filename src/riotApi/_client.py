# encoding: utf-8
from riotApi._lol_static_data import LolStaticData
from riotApi._local_data import LocalData
from riotApi._utils import RateLimitWatcher
from riotApi._championmastery import ChampionMastery
from riotApi._champion import Champion
from riotApi._current_game import CurrentGame


class Client:
    def __init__(self, api_key, production=False, unlimited=False):
        self.api_key = api_key
        self.watcher = RateLimitWatcher(production, unlimited=unlimited)
        self.LolStaticData = LolStaticData(api_key, self.watcher)
        self.LocalData = LocalData(self.LolStaticData)
        self.Championmastery = ChampionMastery(self.api_key, self.watcher)
        self.Champion = Champion(self.api_key, self.watcher)
        self.CurrentGame = CurrentGame(self.api_key, self.watcher)
