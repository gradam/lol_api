# encoding: utf-8
import requests

from lol_api._utils import check_response_code, region_validation


class BaseApiClass:
    def __init__(self, api_key=None, watcher=None, region_default=None, server=()):
        self.api_key = api_key
        self.watcher = watcher
        self.server = server
        self.region_default = region_default.lower()

    def _set_options(self, **kwargs):
        options = {}

        if self.api_key:
            options['api_key'] = self.api_key

        options.update(kwargs)
        return options

    def _get_data(self, url, **kwargs):
        options = self._set_options(**kwargs)
        data = requests.get(url, params=options)
        response_code = data.status_code
        check_response_code(response_code)
        return data.json()

    def _region_to_valid(self, region):
        if region is None:
            return self.region_default
        else:
            return region_validation(region)


