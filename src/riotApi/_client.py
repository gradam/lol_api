# encoding: utf-8
from riotApi._lol_static_data import LolStaticData
from riotApi._local_data import LocalData
from riotApi._utils import RateLimitWatcher


class Client:
    def __init__(self, api_key, production=False):
        self.api_key = api_key
        self.watcher = RateLimitWatcher(production)
        self.LolStaticData = LolStaticData(api_key)
        self.LocalData = LocalData(self.LolStaticData)
