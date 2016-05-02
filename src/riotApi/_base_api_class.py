# encoding: utf-8
import json

import requests

from riotApi._utils import check_response_code


class BaseApiClass:
    def __init__(self, api_key=None, watcher=None):
        self.api_key = api_key
        self.watcher = watcher

    def _set_options(self, **kwargs):
        options = dict()

        if self.api_key:
            options['api_key'] = self.api_key

        options.update(kwargs)
        return options

    def _get_data(self, url, **kwargs):
        options = self._set_options(**kwargs)
        data = requests.get(url, params=options)
        response_code = data.status_code
        check_response_code(response_code)
        return json.loads(data.json())
