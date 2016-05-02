# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import region_default, base_url, api_versions

version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/'.format(base_url)


class LolStaticData(BaseApiClass):
    def champions_all(self, region=region_default, **kwargs):
        """
        Retrieves champion list.
        https://developer.riotgames.com/api/methods#!/1055/3633
        """
        url = '{}{}/{}/champion'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def champion(self, champ_id, region=region_default, **kwargs):
        """
        Retrieves a champion by its id.
        https://developer.riotgames.com/api/methods#!/1055/3622
        """
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
        return self._get_data(url, **kwargs)

    def items_all(self, region=region_default, **kwargs):
        """
        Retrieves item list.
        https://developer.riotgames.com/api/methods#!/1055/3621
        """
        url = '{}{}/{}/item'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def item(self, item_id, region=region_default, **kwargs):
        """
        Retrieves item by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3627
        """
        url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
        return self._get_data(url, **kwargs)

    def language_string(self, region=region_default, **kwargs):
        """
        Retrieve language strings data.
        https://developer.riotgames.com/api/methods#!/1055/3624
        """
        url = '{}{}/{}/language-string'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def languages(self, region=region_default, **kwargs):
        """
        Retrieve supported languages data.
        https://developer.riotgames.com/api/methods#!/1055/3631
        """
        url = '{}{}/{}/languages'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def maps(self, region=region_default, **kwargs):
        """
        Retrieve map data.
        https://developer.riotgames.com/api/methods#!/1055/3635
        """
        url = '{}{}/{}/map'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def mastery_all(self, region=region_default, **kwargs):
        """
        Retrieves mastery list.
        https://developer.riotgames.com/api/methods#!/1055/3625
        """
        url = '{}{}/{}/mastery'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def mastery(self, mastery_id, region=region_default, **kwargs):
        """
        Retrieves mastery item by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3626
        """
        url = '{}{}/{}/mastery/{}'.format(api_url, region, version, mastery_id)
        return self._get_data(url, **kwargs)

    def realm(self, region=region_default, **kwargs):
        """
        Retrieve realm data.
        https://developer.riotgames.com/api/methods#!/1055/3632
        """
        url = '{}{}/{}/realm'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def rune_all(self, region=region_default, **kwargs):
        """
        Retrieves rune list.
        https://developer.riotgames.com/api/methods#!/1055/3623
        """
        url = '{}{}/{}/rune'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def rune(self, rune_id, region=region_default, **kwargs):
        """
        Retrieves rune by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3629
        """
        url = '{}{}/{}/rune/{}'.format(api_url, region, version, rune_id)
        return self._get_data(url, **kwargs)

    def summoner_spell_all(self, region=region_default, **kwargs):
        """
        Retrieves summoner spell list.
        https://developer.riotgames.com/api/methods#!/1055/3634
        """
        url = '{}{}/{}/summoner-spell'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def summoner_spell(self, summoner_spell_id, region=region_default, **kwargs):
        """
        Retrieves summoner spell by its unique id.
        https://developer.riotgames.com/api/methods#!/1055/3628
        """
        url = '{}{}/{}/summoner-spell/{}'.format(api_url, region, version, summoner_spell_id)
        return self._get_data(url, **kwargs)

    def versions(self, region=region_default, **kwargs):
        """
        Retrieve version data.
        https://developer.riotgames.com/api/methods#!/1055/3630
        """
        url = '{}{}/{}/versions'.format(api_url, region, version)
        return self._get_data(url, **kwargs)
