# encoding: utf-8
from lol_api.data import api_versions
from lol_api._utils import get_region, get_data_from_api, base_url

version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/'.format(base_url)
api_url = api_url.format('global')


def champions_all(api_key=None, region=None, **kwargs):
    """
    Retrieves champion list.
    https://developer.riotgames.com/api/methods#!/1055/3633
    """
    region = get_region(region)
    url = '{}{}/{}/champion'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def champion(champ_id, api_key=None, region=None, **kwargs):
    """
    Retrieves a champion by its id.
    https://developer.riotgames.com/api/methods#!/1055/3622
    """
    region = get_region(region)
    url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
    return get_data_from_api(api_key, url, **kwargs)


def items_all(api_key=None, region=None, **kwargs):
    """
    Retrieves item list.
    https://developer.riotgames.com/api/methods#!/1055/3621
    """
    region = get_region(region)
    url = '{}{}/{}/item'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def item(item_id, api_key=None, region=None, **kwargs):
    """
    Retrieves item by its unique id.
    https://developer.riotgames.com/api/methods#!/1055/3627
    """
    region = get_region(region)
    url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
    return get_data_from_api(api_key, url, **kwargs)


def language_string(api_key=None, region=None, **kwargs):
    """
    Retrieve language strings data.
    https://developer.riotgames.com/api/methods#!/1055/3624
    """
    region = get_region(region)
    url = '{}{}/{}/language-string'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def languages(api_key=None, region=None, **kwargs):
    """
    Retrieve supported languages data.
    https://developer.riotgames.com/api/methods#!/1055/3631
    """
    region = get_region(region)
    url = '{}{}/{}/languages'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def maps(api_key=None, region=None, **kwargs):
    """
    Retrieve map data.
    https://developer.riotgames.com/api/methods#!/1055/3635
    """
    region = get_region(region)
    url = '{}{}/{}/map'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def mastery_all(api_key=None, region=None, **kwargs):
    """
    Retrieves mastery list.
    https://developer.riotgames.com/api/methods#!/1055/3625
    """
    region = get_region(region)
    url = '{}{}/{}/mastery'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def mastery(mastery_id, api_key=None, region=None, **kwargs):
    """
    Retrieves mastery item by its unique id.
    https://developer.riotgames.com/api/methods#!/1055/3626
    """
    region = get_region(region)
    url = '{}{}/{}/mastery/{}'.format(api_url, region, version, mastery_id)
    return get_data_from_api(api_key, url, **kwargs)


def realm(api_key=None, region=None, **kwargs):
    """
    Retrieve realm data.
    https://developer.riotgames.com/api/methods#!/1055/3632
    """
    region = get_region(region)
    url = '{}{}/{}/realm'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def rune_all(api_key=None, region=None, **kwargs):
    """
    Retrieves rune list.
    https://developer.riotgames.com/api/methods#!/1055/3623
    """
    region = get_region(region)
    url = '{}{}/{}/rune'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def rune(rune_id, api_key=None, region=None, **kwargs):
    """
    Retrieves rune by its unique id.
    https://developer.riotgames.com/api/methods#!/1055/3629
    """
    region = get_region(region)
    url = '{}{}/{}/rune/{}'.format(api_url, region, version, rune_id)
    return get_data_from_api(api_key, url, **kwargs)


def summoner_spell_all(api_key=None, region=None, **kwargs):
    """
    Retrieves summoner spell list.
    https://developer.riotgames.com/api/methods#!/1055/3634
    """
    region = get_region(region)
    url = '{}{}/{}/summoner-spell'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)


def summoner_spell(summoner_spell_id, api_key=None, region=None, **kwargs):
    """
    Retrieves summoner spell by its unique id.
    https://developer.riotgames.com/api/methods#!/1055/3628
    """
    region = get_region(region)
    url = '{}{}/{}/summoner-spell/{}'.format(api_url, region, version, summoner_spell_id)
    return get_data_from_api(api_key, url, **kwargs)


def versions(api_key=None, region=None, **kwargs):
    """
    Retrieve version data.
    https://developer.riotgames.com/api/methods#!/1055/3630
    """
    region = get_region(region)
    url = '{}{}/{}/versions'.format(api_url, region, version)
    return get_data_from_api(api_key, url, **kwargs)
