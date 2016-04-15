# encoding: utf-8

import requests

from riotApi import api_key, region_default, base_url
from riotApi.utils import check_response_code

version = 'v1.2'

api_url = '{}/api/lol/static-data/'.format(base_url)


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


def every_champions_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3633
    :param region: eg. eune
    :param kwargs: optional parameters for LoL Api
    :return: json data
    not counted in Rate Limit.
    """
    url = '{}{}/{}/champion'.format(api_url, region, version)
    data = _get_data(url, kwargs)
    return data.json()


def champion_info(champ_id, region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3622
    :param champ_id: id of a champion
    :param region: eg. eune
    :param kwargs: optional parameters for LoL Api
    :return: json data
    not counted in Rate Limit.
    """
    url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
    data = _get_data(url, kwargs)
    return data.json()


def item_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3621
    :param region: eg. eune
    :param kwargs: optional parameters for LoL Api
    :return: json data
    not counted in Rate Limit
    """
    url = '{}{}/{}/item'.format(api_key, region, version)
    data = _get_data(url, kwargs)
    return data.json()
