# encoding: utf-8
from lol_api._utils import get_region, get_data_from_api,  count_request, base_url
from lol_api.data import api_versions

version = api_versions['stats']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def ranked(summoner_id, api_key=None, region=None, **kwargs):
    """
    Get ranked stats by summoner ID.
    https://developer.riotgames.com/api/methods#!/1080/3725
    """
    region = get_region(region)
    url = '{}{}/{}/stats/by-summoner/{}/ranked'.format(api_url, region, version, summoner_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)

@count_request
def summary(summoner_id, api_key=None, region=None, **kwargs):
    """
    Get player stats summaries by summoner ID.
    https://developer.riotgames.com/api/methods#!/1080/3726
    """
    region = get_region(region)
    url = '{}{}/{}/stats/by-summoner/{}/summary'.format(api_url, region, version, summoner_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)

