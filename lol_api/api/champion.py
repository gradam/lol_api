# encoding: utf-8
from lol_api.utils import get_region, get_data_from_api,  count_request, base_url, get_region, get_data_from_api
from lol_api.data import api_versions

version = api_versions['champion']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def champions_all(api_key=None, region=None, **kwargs):
    """
    Retrieve all champions.
    https://developer.riotgames.com/api/methods#!/1077/3717
    """
    region = get_region(region)
    url = '{}{}/{}/champion'.format(api_url, region, version)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)


@count_request
def champion(champion_id, api_key=None, region=None, **kwargs):
    """
    Retrieve champion by ID.
    https://developer.riotgames.com/api/methods#!/1077/3716
    """
    region = get_region(region)
    url = '{}{}/{}/champion/{}'.format(api_url, region, version, champion_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)
