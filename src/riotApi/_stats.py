# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, base_url
from riotApi.data import region_default, api_versions

version = api_versions['stats']
api_url = '{}/api/lol/'.format(base_url)


class Stats(BaseApiClass):

    @count_request
    def ranked(self, summoner_id, region=region_default, **kwargs):
        """
        Get ranked stats by summoner ID.
        https://developer.riotgames.com/api/methods#!/1080/3725
        """
        url = '{}{}/{}/stats/by-summoner/{}/ranked'.format(api_url, region, version, summoner_id)
        return self._get_data(url, **kwargs)

    @count_request
    def summary(self, summoner_id, region=region_default, **kwargs):
        """
        Get player stats summaries by summoner ID.
        https://developer.riotgames.com/api/methods#!/1080/3726
        """
        url = '{}{}/{}/stats/by-summoner/{}/summary'.format(api_url, region, version,summoner_id)
        return self._get_data(url, **kwargs)

