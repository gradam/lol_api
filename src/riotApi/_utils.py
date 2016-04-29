# encoding: utf-8

import os
import requests
from collections import defaultdict, deque, namedtuple
import time

from riotApi.exceptions import RateLimitExceededError


error_codes = defaultdict(lambda: 'Unknown error code', )

error_codes.update({
    204: 'no masteries found for given player id or player id and champion id combination.',
    400: 'Bad request',
    401: 'Unauthorized',
    404: 'Data not found',
    429: 'Rate limit exceeded',
    500: 'Internal server error',
    503: 'Service unavailable',
})
base_url = 'https://global.api.pvp.net'

directory = os.path.dirname(os.path.realpath(__file__))

regions = {
    'brazil': 'br',
    'europe_nordic_east': 'eune',
    'europe_west': 'euw',
    'korea': 'kr',
    'latin_america_north': 'lan',
    'latin_america_south': 'las',
    'north_america': 'na',
    'oceania': 'oce',
    'russia': 'ru',
    'turkey': 'tr',
}

region_default = regions['europe_nordic_east']

platforms = {
    'br': 'BR1',
    'eune': 'EUN1',
    'uew': 'EUW1',
    'kr': 'KR',
    'lan': 'LA1',
    'las': 'LA2',
    'na': 'NA1',
    'oce': 'OC1',
    'ru': 'RU',
    'tr': 'TR1'
}

queue_types = [
    'CUSTOM',  # Custom games
    'NORMAL_5x5_BLIND',  # Normal 5v5 blind pick
    'BOT_5x5',  # Historical Summoners Rift coop vs AI games
    'BOT_5x5_INTRO',  # Summoners Rift Intro bots
    'BOT_5x5_BEGINNER',  # Summoner's Rift Coop vs AI Beginner Bot games
    'BOT_5x5_INTERMEDIATE',  # Historical Summoner's Rift Coop vs AI Intermediate Bot games
    'NORMAL_3x3',  # Normal 3v3 games
    'NORMAL_5x5_DRAFT',  # Normal 5v5 Draft Pick games
    'ODIN_5x5_BLIND',  # Dominion 5v5 Blind Pick games
    'ODIN_5x5_DRAFT',  # Dominion 5v5 Draft Pick games
    'BOT_ODIN_5x5',  # Dominion Coop vs AI games
    'RANKED_SOLO_5x5',  # Ranked Solo 5v5 games
    'RANKED_PREMADE_3x3',  # Ranked Premade 3v3 games
    'RANKED_PREMADE_5x5',  # Ranked Premade 5v5 games
    'RANKED_TEAM_3x3',  # Ranked Team 3v3 games
    'RANKED_TEAM_5x5',  # Ranked Team 5v5 games
    'BOT_TT_3x3',  # Twisted Treeline Coop vs AI games
    'GROUP_FINDER_5x5',  # Team Builder games
    'ARAM_5x5',  # ARAM games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1v1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2v2 games
    'SR_6x6',  # Hexakill games
    'URF_5x5',  # Ultra Rapid Fire games
    'BOT_URF_5x5',  # Ultra Rapid Fire games played against AI games
    'NIGHTMARE_BOT_5x5_RANK1',  # Doom Bots Rank 1 games
    'NIGHTMARE_BOT_5x5_RANK2',  # Doom Bots Rank 2 games
    'NIGHTMARE_BOT_5x5_RANK5',  # Doom Bots Rank 5 games
    'ASCENSION_5x5',  # Ascension games
    'HEXAKILL',  # 6v6 games on twisted treeline
    'KING_PORO_5x5',  # King Poro game games
    'COUNTER_PICK',  # Nemesis games,
    'BILGEWATER_5x5',  # Black Market Brawlers games
]

api_versions = {
    'champion': 'v1.2',
    'current-game': 'v1.0',
    'featured-games': 'v1.0',
    'game': 'v1.3',
    'league': 'v2.5',
    'lol-static-data': 'v1.2',
    'lol-status': 'v1.0',
    'match': 'v2.2',
    'matchlist': 'v2.2',
    'stats': 'v1.3',
    'summoner': 'v1.4',
    'team': 'v2.4',
}


class RateLimitWatcher:
    def __init__(self, production, unlimited=False):
        self.unlimited = unlimited
        Limit = namedtuple('Limits', ['requests', 'seconds'])
        if production:
            self.short_limit = Limit(requests=3000, seconds=10)
            self.long_limit = Limit(requests=180000, seconds=600)
        else:
            self.short_limit = Limit(requests=10, seconds=10)
            self.long_limit = Limit(requests=500, seconds=600)
        self.made_requests = deque(maxlen=self.long_limit.requests)

    def add_request(self):
        self.made_requests.append(time.time())

    def _reload(self):
        t = time.time() - 600
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def request_available(self):
        self._reload()
        if self.unlimited:
            return True
        try:
            latest_short_requests = self.made_requests[self.short_limit.requests - 1]
        except IndexError:
            latest_short_requests = time.time() - 30
        requests_limit = self.long_limit.requests
        if latest_short_requests < time.time() - 10 and len(self.made_requests) != requests_limit:
            return True
        else:
            return False


def check_response_code(response_code):
    if response_code != 200:
        error_massage = 'Error code: {} - {}'.format(response_code, error_codes[response_code])
        raise requests.RequestException(error_massage)


def count_request(func):
    def wrapper(self, *args, **kwargs):
        if self.watcher.request_available():
            self.watcher.add_request()
            return func(self, *args, **kwargs)
        else:
            raise RateLimitExceededError

    return wrapper


def get_champion_id(value):
    try:
        value = int(value)
        return value
    except ValueError:
        pass
