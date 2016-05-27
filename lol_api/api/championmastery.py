# encoding: utf-8
from lol_api._utils import get_region, get_data_from_api,  count_request, get_champion_id, base_url, get_region, get_data_from_api
from lol_api.data import platforms

api_url = '{}/championmastery/location/'.format(base_url)


@count_request
def champion_master(player_id, champion, api_key=None, region=None, **kwargs):
    """
    Get a champion mastery by player id and champion id.
    https://developer.riotgames.com/api/methods#!/1071/3697
    """
    region = get_region(region)
    champion_id = get_champion_id(champion)
    platform = platforms[region]
    url = '{}{}/player/{}/champion/{}'.format(api_url, platform, player_id, champion_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def champions_points(player_id, api_key=None, region=None, **kwargs):
    """
    Get all champion mastery entries.
    https://developer.riotgames.com/api/methods#!/1071/3696
    """
    region = get_region(region)
    platform = platforms[region]
    url = '{}{}/player/{}/champions'.format(api_url, platform, player_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def score(player_id, api_key=None, region=None, **kwargs):
    """
    Get a player's total champion mastery score.
    https://developer.riotgames.com/api/methods#!/1071/3698
    """
    region = get_region(region)
    platform = platforms[region]
    url = '{}{}/player/{}/score'.format(api_url, platform, player_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def top_champions(player_id, api_key=None, region=None, **kwargs):
    """
    Get specified number of top champion mastery entries
    https://developer.riotgames.com/api/methods#!/1071/3692
    """
    region = get_region(region)
    platform = platforms[region]
    url = '{}{}/player/{}/topchampions'.format(api_url, platform, player_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)

