# encoding: utf-8
from collections import namedtuple

import requests

from riotApi import error_codes
from riotApi.static_info import ID_to_name, name_to_ID


def check_response_code(response_code):
    if response_code != 200:
        error_massage = 'Error code: {} - {}'.format(response_code, error_codes[response_code])
        raise requests.RequestException(error_massage)


def get_champion_info(value):
    Champ = namedtuple('Champion', ['ID', 'name'])
    try:
        ID = int(value)
        return Champ(ID, ID_to_name[ID])
    except ValueError:
        name = value.lower()
        return Champ(name_to_ID[name], name)