# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request
from riotApi._utils import region_default


class FeaturedGames(BaseApiClass):
    @count_request
    def featured(self, region=region_default, **kwargs):
        """
        Get list of featured games.
        https://developer.riotgames.com/api/methods#!/977/3337
        """
        url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region)
        return self._get_data(url, **kwargs)
