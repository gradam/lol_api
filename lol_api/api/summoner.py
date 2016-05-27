# encoding: utf-8
from lol_api._utils import get_region, get_data_from_api, count_request, to_comma_separated, \
    base_url
from lol_api.data import api_versions

version = api_versions['summoner']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def by_name(summoner_names, api_key=None, region=None, **kwargs):
    """
    Get summoner objects mapped by standardized summoner name for a given list of summoner names.
    https://developer.riotgames.com/api/methods#!/1079/3722
    :param  summoner_names: can be both list or string in valid format
    """
    region = get_region(region)
    names = to_comma_separated(summoner_names)
    url = '{}{}/{}/summoner/by-name/{}'.format(api_url, region, version, names)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def by_id(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get summoner objects mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/1079/3724
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/summoner/{}'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def masteries(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get mastery pages mapped by summoner ID for a given list of summoner IDs
    https://developer.riotgames.com/api/methods#!/1079/3723
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/summoner/{}/masteries'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def name(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get summoner names mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/1079/3720
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/summoner/{}/name'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def runes(summoner_ids, api_key=None, region=None, **kwargs):
    """
    Get rune pages mapped by summoner ID for a given list of summoner IDs.
    https://developer.riotgames.com/api/methods#!/1079/3719
    :param summoner_ids: can be both list or string in valid format
    """
    region = get_region(region)
    ids = to_comma_separated(summoner_ids)
    url = '{}{}/{}/summoner/{}/runes'.format(api_url, region, version, ids)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)
