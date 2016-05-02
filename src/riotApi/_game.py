# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions, count_request
from riotApi._base_api_class import BaseApiClass

version = api_versions['game']
api_url = '{}/api/lol/'.format(base_url)


class Game(BaseApiClass):
    @count_request
    def recent(self, summoner_id, region=region_default, **kwargs):
        """
        Get recent games by summoner ID.
        https://developer.riotgames.com/api/methods#!/1078/3718
        """
        url = '{}{}/{}/game/by-summoner/{}/recent'.format(api_url, region, version, summoner_id)
        return self._get_data(url, **kwargs)
