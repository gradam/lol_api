# encoding: utf-8

import requests

from riotApi._utils import region_default, base_url, api_versions
from riotApi._utils import check_response_code

version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/'.format(base_url)


class LolStaticData:
    def __init__(self, api_key):
        self.api_key = api_key

    def _set_options(self, kwargs):
        options = {'api_key': self.api_key}
        options.update(kwargs)
        return options

    def _get_data(self, url, kwargs):
        options = self._set_options(kwargs)
        data = requests.get(url, params=options)
        response_code = data.status_code
        check_response_code(response_code)
        return data

    def all_champions_info(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3633
        :return: json data
        not counted in Rate Limit.
        """
        url = '{}{}/{}/champion'.format(api_url, region, version)
        data = self._get_data(url, kwargs)
        return data.json()

    def champion_info(self, champ_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3622
        :return: json data
        not counted in Rate Limit.
        """
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
        data = self._get_data(url, kwargs)
        return data.json()

    def all_items_info(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3621
        :return: json data
        """
        url = '{}{}/{}/item'.format(api_url, region, version)
        data = self._get_data(url, kwargs)
        return data.json()

    def item_info(self, item_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3627
        :return: json data
        """
        url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
        data = self._get_data(url, kwargs)
        return data.json()
