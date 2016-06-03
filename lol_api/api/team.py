# encoding: utf-8
from lol_api.utils import get_region, get_data_from_api,  count_request, to_comma_separated, base_url, get_region, get_data_from_api
from lol_api.data import api_versions

version = api_versions['team']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def by_summoners(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get teams mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/986/3358
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/team/by-summoner/{}'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def by_teams(team_ids, api_key=None, region=None, **kwargs):
    """
    Get teams mapped by team ID for a given list of team IDs.
    https://developer.riotgames.com/api/methods#!/986/3357
    :param team_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(team_ids)
    url = '{}{}/{}/team/{}'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)
