# encoding: utf-8
from lol_api._utils import get_region, get_data_from_api,  count_request, base_url
from lol_api.data import api_versions

version = api_versions['match']
api_url = '{}/api/lol/'.format(base_url)


@count_request
def match(match_id, api_key=None, region=None, **kwargs):
    """
    Retrieve match by match ID.
    https://developer.riotgames.com/api/methods#!/1064/3671
    """
    region = get_region(region)
    url = '{}{}/{}/match/{}'.format(api_url, region, version, match_id)
    url = url.format(region)
    return get_data_from_api(api_key, url, **kwargs)



