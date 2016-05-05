# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, base_url
from riotApi.data import api_versions

version = api_versions['champion']
api_url = '{}/api/lol/'.format(base_url)


class Champion(BaseApiClass):
    @count_request
    def champions_all(self, region=None, **kwargs):
        """
        Retrieve all champions.
        https://developer.riotgames.com/api/methods#!/1077/3717
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/champion'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    @count_request
    def champion(self, champion_id, region=None, **kwargs):
        """
        Retrieve champion by ID.
        https://developer.riotgames.com/api/methods#!/1077/3716
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champion_id)
        return self._get_data(url, **kwargs)
