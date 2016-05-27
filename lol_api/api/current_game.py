# encoding: utf-8
from lol_api._utils import get_region, get_data_from_api,  count_request, base_url
from lol_api.data import platforms

api_url = '{}/observer-mode/rest/consumer/getSpectatorGameInfo'.format(base_url)


@count_request
def spectator_game_info(summoner_id, api_key=None, region=None, **kwargs):
    """
    Get current game information for the given summoner ID
    https://developer.riotgames.com/api/methods#!/976/3336
    """
    region = get_region(region)
    platform = platforms[region]
    url = '{}/{}/{}'.format(api_url, platform, summoner_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)

