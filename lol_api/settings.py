# encoding: utf-8
from lol_api.rate_limit_watcher import RateLimitWatcher


class Settings:
    def __init__(self):
        self.API_KEY = None
        self.REGION_DEFAULT = None
        self.DAEMON_SERVER = ()
        self.WATCHER = None

    def initialize_watcher(self, unlimited=False, production=False):
        self.WATCHER = RateLimitWatcher(unlimited=unlimited, production=production)


settings = Settings()
