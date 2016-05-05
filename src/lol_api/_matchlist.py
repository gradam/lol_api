# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api._utils import count_request, base_url
from lol_api.data import api_versions

version = api_versions['matchlist']
api_url = '{}/api/lol/'.format(base_url)


class Matchlist(BaseApiClass):

    @count_request
    def by_summoner(self, summoner_id, region=None, **kwargs):
        """
        Retrieve match list by summoner ID.
        https://developer.riotgames.com/api/methods#!/1069/3683
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/matchlist/by-summoner/{}'.format(api_url, region, version, summoner_id)
        return self._get_data(url, **kwargs)
