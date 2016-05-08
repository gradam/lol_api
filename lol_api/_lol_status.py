# encoding: utf-8
# encoding: utf-8
from lol_api._base_api_class import BaseApiClass

api_url = 'http://status.leagueoflegends.com/shards'


class LolStatus(BaseApiClass):

    def shards(self, **kwargs):
        """
        Get shard list.
        https://developer.riotgames.com/api/methods#!/908/3143
        """
        url = '{}'.format(api_url)
        return self._get_data(url, **kwargs)

    def shards_region(self, region=None, **kwargs):
        """
        Get shard status. Returns the data available on the status.leagueoflegends.com website for the given region.
        https://developer.riotgames.com/api/methods#!/908/3142
        """
        region = self._region_to_valid(region)
        url = '{}/{}'.format(api_url, region)
        return self._get_data(url, **kwargs)

