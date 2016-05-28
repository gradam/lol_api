# encoding: utf-8
from collections import defaultdict

error_codes = defaultdict(lambda: 'Unknown error code', )

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

error_codes.update({
    204: 'no masteries found for given player id or player id and champion id combination.',
    400: 'Bad request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Data not found',
    429: 'Rate limit exceeded',
    500: 'Internal server error',
    503: 'Service unavailable',
})

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

queue_types = {
    'CUSTOM': 'Custom games',
    'NORMAL_5x5_BLIND': 'Normal 5v5 blind pick',
    'BOT_5x5': 'Historical Summoners Rift coop vs AI games',
    'BOT_5x5_INTRO': 'Summoners Rift Intro bots',
    'BOT_5x5_BEGINNER': "Summoner's Rift Coop vs AI Beginner Bot games",
    'BOT_5x5_INTERMEDIATE': "Historical Summoner's Rift Coop vs AI Intermediate Bot games",
    'NORMAL_3x3': 'Normal 3v3 games',
    'NORMAL_5x5_DRAFT': 'Normal 5v5 Draft Pick games',
    'ODIN_5x5_BLIND': 'Dominion 5v5 Blind Pick games',
    'ODIN_5x5_DRAFT': 'Dominion 5v5 Draft Pick games',
    'BOT_ODIN_5x5': 'Dominion Coop vs AI games',
    'RANKED_SOLO_5x5': 'Ranked Solo 5v5 games',
    'RANKED_PREMADE_3x3': 'Ranked Premade 3v3 games',
    'RANKED_PREMADE_5x5': 'Ranked Premade 5v5 games',
    'RANKED_TEAM_3x3': 'Ranked Team 3v3 games',
    'RANKED_TEAM_5x5': 'Ranked Team 5v5 games',
    'BOT_TT_3x3': 'Twisted Treeline Coop vs AI games',
    'GROUP_FINDER_5x5': 'Team Builder games',
    'ARAM_5x5': 'ARAM games',
    'ONEFORALL_5x5': 'One for All games',
    'FIRSTBLOOD_1x1': 'Snowdown Showdown 1v1 games',
    'FIRSTBLOOD_2x2': 'Snowdown Showdown 2v2 games',
    'SR_6x6': 'Hexakill games',
    'URF_5x5': 'Ultra Rapid Fire games',
    'BOT_URF_5x5': 'Ultra Rapid Fire games played against AI games',
    'NIGHTMARE_BOT_5x5_RANK1': 'Doom Bots Rank 1 games',
    'NIGHTMARE_BOT_5x5_RANK2': 'Doom Bots Rank 2 games',
    'NIGHTMARE_BOT_5x5_RANK5': 'Doom Bots Rank 5 games',
    'ASCENSION_5x5': 'Ascension games',
    'HEXAKILL': '6v6 games on twisted treeline',
    'KING_PORO_5x5': 'King Poro game games',
    'COUNTER_PICK': 'Nemesis games,',
    'BILGEWATER_5x5': 'Black Market Brawlers games',
}
