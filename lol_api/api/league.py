# encoding: utf-8
from lol_api.utils import get_region, get_data_from_api, count_request, to_comma_separated, \
    base_url
from lol_api.data import api_versions

version = api_versions['league']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def by_summoners(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get leagues mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/985/3351
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/league/by-summoner/{}'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def by_summoners_entry(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get league entries mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/985/3356
    :param summoner_ids: can be both list or string in valid formats
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/league/by-summoner/{}/entry'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def by_teams(team_ids, api_key=None, region=None, **kwargs):
    """
    Get leagues mapped by team ID for a given list of team IDs.
    https://developer.riotgames.com/api/methods#!/985/3352
    :param team_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(team_ids)
    url = '{}{}/{}/league/by-team/{}'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def by_teams_entry(team_ids, api_key=None, region=None, **kwargs):
    """
    Get league entries mapped by team ID for a given list of team IDs.
    https://developer.riotgames.com/api/methods#!/985/3355
    :param team_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(team_ids)
    url = '{}{}/{}/league/by-team/{}/entry'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def challenger(api_key=None, region=None, **kwargs):
    """
    Get challenger tier leagues.
    https://developer.riotgames.com/api/methods#!/985/3353
    """
    region = get_region(region)
    url = '{}{}/{}/league/challenger'.format(api_url, region, version)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def master(api_key=None, region=None, **kwargs):
    """
    Get master tier leagues.
    https://developer.riotgames.com/api/methods#!/985/3354
    """
    region = get_region(region)
    url = '{}{}/{}/league/master'.format(api_url, region, version)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)
