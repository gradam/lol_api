# encoding: utf-8

import requests

from riotApi import api_key, region_default, error_codes, base_url


def get_every_champions_info(region=region_default, **kwargs):
    """
    https://developer.riotgames.com/api/methods#!/1055/3633
    :param region: LoL server
    :param kwargs: optional parameters for api request
    :return: json data
    """
    options = {'api_key': api_key}
    options.update(kwargs)

    url = '{}/api/lol/static-data/{}/v1.2/champion'.format(base_url, region)
    data = requests.get(url, params=options)
    response_code = data.status_code
    if response_code != 200:
        error_massage = 'Error code: {} - {}'.format(response_code, error_codes[response_code])
        raise requests.RequestException(error_massage)
    return data.json()
