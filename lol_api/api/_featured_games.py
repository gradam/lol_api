# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api._utils import count_request


class FeaturedGames(BaseApiClass):
    @count_request
    def featured(self, region=None, **kwargs):
        """
        Get list of featured games.
        https://developer.riotgames.com/api/methods#!/977/3337
        """
        region = self._region_to_valid(region)
        url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region)
        return self._get_data(url, **kwargs)
