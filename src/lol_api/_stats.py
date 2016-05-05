# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api._utils import count_request, base_url
from lol_api.data import api_versions

version = api_versions['stats']
api_url = '{}/api/lol/'.format(base_url)


class Stats(BaseApiClass):

    @count_request
    def ranked(self, summoner_id, region=None, **kwargs):
        """
        Get ranked stats by summoner ID.
        https://developer.riotgames.com/api/methods#!/1080/3725
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/stats/by-summoner/{}/ranked'.format(api_url, region, version, summoner_id)
        return self._get_data(url, **kwargs)

    @count_request
    def summary(self, summoner_id, region=None, **kwargs):
        """
        Get player stats summaries by summoner ID.
        https://developer.riotgames.com/api/methods#!/1080/3726
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/stats/by-summoner/{}/summary'.format(api_url, region, version,summoner_id)
        return self._get_data(url, **kwargs)

