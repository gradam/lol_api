# encoding: utf-8
from lol_api.utils import get_region, get_data_from_api,  count_request


@count_request
def featured(api_key=None, region=None, **kwargs):
    """
    Get list of featured games.
    https://developer.riotgames.com/api/methods#!/977/3337
    """
    region = get_region(region)
    url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region)
    return get_data_from_api(api_key, url, **kwargs)
