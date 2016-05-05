# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, base_url
from riotApi.data import platforms

api_url = '{}/observer-mode/rest/consumer/getSpectatorGameInfo'.format(base_url)


class CurrentGame(BaseApiClass):
    @count_request
    def spectator_game_info(self, summoner_id, region=None, **kwargs):
        """
        Get current game information for the given summoner ID
        https://developer.riotgames.com/api/methods#!/976/3336
        """
        region = self._region_to_valid(region)
        platform = platforms[region]
        url = '{}/{}/{}'.format(api_url, platform, summoner_id)
        return self._get_data(url, **kwargs)

