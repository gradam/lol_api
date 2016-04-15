# encoding: utf-8

import requests

from riotApi import api_key, region_default, base_url
from riotApi.utils import check_response_code

version = 'v1.2'
api_url = '{}/api/lol/static-data/'.format(base_url)
counted = False


def _get_options(kwargs):
    options = {'api_key': api_key}
    options.update(kwargs)
    return options


def _get_data(url, kwargs):
    options = _get_options(kwargs)
    data = requests.get(url, params=options)
    response_code = data.status_code
    check_response_code(response_code)
    return data


def all_champions_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3633
    :return: json data
    not counted in Rate Limit.
    """
    url = '{}{}/{}/champion'.format(api_url, region, version)
    data = _get_data(url, kwargs)
    return data.json()


def champion_info(champ_id, region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3622
    :return: json data
    not counted in Rate Limit.
    """
    url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
    data = _get_data(url, kwargs)
    return data.json()


def all_items_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3621
    :return: json data
    """
    url = '{}{}/{}/item'.format(api_url, region, version)
    data = _get_data(url, kwargs)
    return data.json()


def item_info(item_id, region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3627
    :return: json data
    """
    url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
    data = _get_data(url, kwargs)
    return data.json()
