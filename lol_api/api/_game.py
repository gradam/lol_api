# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api._utils import count_request, base_url
from lol_api.data import api_versions

version = api_versions['game']
api_url = '{}/api/lol/'.format(base_url)


class Game(BaseApiClass):
    @count_request
    def recent(self, summoner_id, region=None, **kwargs):
        """
        Get recent games by summoner ID.
        https://developer.riotgames.com/api/methods#!/1078/3718
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/game/by-summoner/{}/recent'.format(api_url, region, version, summoner_id)
        url = url.format(region)
        return self._get_data(url, **kwargs)
