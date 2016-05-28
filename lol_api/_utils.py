# encoding: utf-8

import os
import json
import socket

import requests

from lol_api.data import error_codes, regions
from lol_api.exceptions import *
from lol_api.settings import settings

base_url = 'https://{}.api.pvp.net'


def check_response_code(response_code, url):
    if response_code != 200:
        error_massage = 'Error code: {} - {}\nurl={}'.format(response_code,
                                                             error_codes[response_code], url)
        raise requests.RequestException(error_massage)


def send_request_to_daemon(api_key, region, server):
    data = json.dumps({
        'api_key': api_key,
        'region': region
    })
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(server)
    sock.sendall(bytes(data, 'utf-8'))

    received_data = sock.recv(1024).decode('utf-8')
    response = json.loads(received_data)['available']

    return response


def get_champion_id(value):
    try:
        value = int(value)
        return value
    except ValueError:
        raise NotImplementedError
        # TODO: get champion ID from name


def to_comma_separated(ids):
    if isinstance(ids, str):
        return ids
    elif isinstance(ids, int):
        return str(ids)
    else:
        return ','.join([str(x) for x in ids])


def region_validation(region):
    region = region.lower()
    try:
        return regions[region]
    except KeyError:
        if region in regions.values():
            return region
    raise InvalidRegionError


def get_data_from_api(api_key, url, **kwargs):
    kwargs['api_key'] = get_api_key(api_key)
    data = requests.get(url, params=kwargs)
    response_code = data.status_code
    check_response_code(response_code, url)
    return data.json()


def get_api_key(api_key):
    if not (api_key or settings.API_KEY):
        try:
            return os.environ['LOL_API_KEY']
        except KeyError:
            raise NoApiKeySpecified

    return api_key if api_key else settings.API_KEY


def get_region(region_default=None):
    if region_default:
        return region_validation(region_default)
    elif settings.REGION_DEFAULT:
        return settings.REGION_DEFAULT
    else:
        raise RegionDefaultNotSpecified


def count_request(func):
    def wrapper(*args, **kwargs):
        try:
            region = kwargs['region']
            region_validation(region)
        except KeyError:
            region = get_region()

        if settings.DAEMON_SERVER:
            is_available = send_request_to_daemon(settings.API_KEY, region, settings.DAEMON_SERVER)
        else:
            if settings.WATCHER.request_available(region):
                is_available = True
                settings.WATCHER.add_request(region)
            else:
                is_available = False

        if is_available:
            return func(*args, **kwargs)
        else:
            raise RateLimitExceededError

    return wrapper
