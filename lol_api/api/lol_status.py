# encoding: utf-8
# encoding: utf-8
from lol_api._utils import get_data_from_api, get_region
api_url = 'http://status.leagueoflegends.com/shards'


def shards(api_key=None, **kwargs):
    """
    Get shard list.
    https://developer.riotgames.com/api/methods#!/908/3143
    """
    url = '{}'.format(api_url)
    return get_data_from_api(api_key, url, **kwargs)


def shards_region(api_key=None, region=None, **kwargs):
    """
    Get shard status. Returns the data available on the status.leagueoflegends.com website for the given region.
    https://developer.riotgames.com/api/methods#!/908/3142
    """
    region = get_region(region)
    url = '{}/{}'.format(api_url, region)
    return get_data_from_api(api_key, url, **kwargs)

