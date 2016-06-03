# encoding: utf-8
from lol_api.utils import get_region, get_data_from_api,  count_request, base_url
from lol_api.data import api_versions

version = api_versions['matchlist']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def by_summoner(summoner_id, api_key=None, region=None, **kwargs):
    """
    Retrieve match list by summoner ID.
    https://developer.riotgames.com/api/methods#!/1069/3683
    """
    region = get_region(region)
    url = '{}{}/{}/matchlist/by-summoner/{}'.format(api_url, region, version, summoner_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)
