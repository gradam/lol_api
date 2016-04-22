# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request

version = api_versions['champion']
api_url = '{}/api/lol/'.format(base_url)


class Champion(BaseApiClass):
    @count_request
    def champions_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1077/3717
        """
        url = '{}{}/{}/champion'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    @count_request
    def champion(self, champion_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1077/3716
        """
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champion_id)
        return self._get_data(url, kwargs)
