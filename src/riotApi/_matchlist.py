# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions, count_request
from riotApi._base_api_class import BaseApiClass

version = api_versions['matchlist']
api_url = '{}/api/lol/'.format(base_url)


class Matchlist(BaseApiClass):

    @count_request
    def by_summoner(self, summoner_id, region=region_default, **kwargs):
        """
        Retrieve match list by summoner ID.
        https://developer.riotgames.com/api/methods#!/1069/3683
        """
        url = '{}{}/{}/matchlist/by-summoner/{}'.format(api_url, region, version, summoner_id)
        return self._get_data(url, **kwargs)
