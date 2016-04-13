# encoding: utf-8

import requests

from riotApi import api_key, region_default, base_url
from .utils import check_response_code

version = 'v1.2'

api_url = '{}/api/lol/static-data/'.format(base_url)


def get_every_champions_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3633
    :param region: eg. eune
    :param kwargs: optional parameters for LoL Api
    :return: json data
    not counted in your Rate Limit.
    """
    options = {'api_key': api_key}
    options.update(kwargs)

    url = '{}{}/{}/champion'.format(api_url, region, version)
    data = requests.get(url, params=options)
    response_code = data.status_code
    check_response_code(response_code)
    return data.json()

#
# def get_champion_info(id, region=region_default, **kwargs):
#     """
#     https://developer.riotgames.com/api/methods#!/1055/3633
#     :param id: id of a champion
#     :param region: eg. eune
#     :param kwargs: optional parameters for LoL Api
#     :return: json data
#     not counted in your Rate Limit.
#     """
#     pass