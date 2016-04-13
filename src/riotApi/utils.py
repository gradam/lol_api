# encoding: utf-8
import os

import requests

from riotApi import error_codes


def check_response_code(response_code):
    if response_code != 200:
        error_massage = 'Error code: {} - {}'.format(response_code, error_codes[response_code])
        raise requests.RequestException(error_massage)
