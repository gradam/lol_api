# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api.data import api_versions
from lol_api._utils import base_url

version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/'.format(base_url)
api_url = api_url.format('global')


class LolStaticData(BaseApiClass):
    def champions_all(self, region=None, **kwargs):
        """
        Retrieves champion list.
        https://developer.riotgames.com/api/methods#!/1055/3633
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/champion'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def champion(self, champ_id, region=None, **kwargs):
        """
        Retrieves a champion by its id.
        https://developer.riotgames.com/api/methods#!/1055/3622
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
        return self._get_data(url, **kwargs)

    def items_all(self, region=None, **kwargs):
        """
        Retrieves item list.
        https://developer.riotgames.com/api/methods#!/1055/3621
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/item'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def item(self, item_id, region=None, **kwargs):
        """
        Retrieves item by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3627
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
        return self._get_data(url, **kwargs)

    def language_string(self, region=None, **kwargs):
        """
        Retrieve language strings data.
        https://developer.riotgames.com/api/methods#!/1055/3624
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/language-string'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def languages(self, region=None, **kwargs):
        """
        Retrieve supported languages data.
        https://developer.riotgames.com/api/methods#!/1055/3631
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/languages'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def maps(self, region=None, **kwargs):
        """
        Retrieve map data.
        https://developer.riotgames.com/api/methods#!/1055/3635
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/map'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def mastery_all(self, region=None, **kwargs):
        """
        Retrieves mastery list.
        https://developer.riotgames.com/api/methods#!/1055/3625
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/mastery'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def mastery(self, mastery_id, region=None, **kwargs):
        """
        Retrieves mastery item by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3626
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/mastery/{}'.format(api_url, region, version, mastery_id)
        return self._get_data(url, **kwargs)

    def realm(self, region=None, **kwargs):
        """
        Retrieve realm data.
        https://developer.riotgames.com/api/methods#!/1055/3632
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/realm'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def rune_all(self, region=None, **kwargs):
        """
        Retrieves rune list.
        https://developer.riotgames.com/api/methods#!/1055/3623
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/rune'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def rune(self, rune_id, region=None, **kwargs):
        """
        Retrieves rune by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3629
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/rune/{}'.format(api_url, region, version, rune_id)
        return self._get_data(url, **kwargs)

    def summoner_spell_all(self, region=None, **kwargs):
        """
        Retrieves summoner spell list.
        https://developer.riotgames.com/api/methods#!/1055/3634
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/summoner-spell'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def summoner_spell(self, summoner_spell_id, region=None, **kwargs):
        """
        Retrieves summoner spell by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3628
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/summoner-spell/{}'.format(api_url, region, version, summoner_spell_id)
        return self._get_data(url, **kwargs)

    def versions(self, region=None, **kwargs):
        """
        Retrieve version data.
        https://developer.riotgames.com/api/methods#!/1055/3630
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/versions'.format(api_url, region, version)
        return self._get_data(url, **kwargs)
