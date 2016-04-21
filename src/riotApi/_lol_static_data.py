# encoding: utf-8

import requests

from riotApi._utils import region_default, base_url, api_versions
from riotApi._base_api_class import BaseApiClass

version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/'.format(base_url)


class LolStaticData(BaseApiClass):
    def champions_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3633
        not counted in Rate Limit.
        """
        url = '{}{}/{}/champion'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def champion(self, champ_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3622
        not counted in Rate Limit.
        """
        url = '{}{}/{}/champion/{}'.format(api_url, region, version, champ_id)
        return self._get_data(url, kwargs)

    def items_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3621
        not counted in Rate Limit.
        """
        url = '{}{}/{}/item'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def item(self, item_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3627
        not counted in Rate Limit.
        """
        url = '{}{}/{}/item/{}'.format(api_url, region, version, item_id)
        return self._get_data(url, kwargs)

    def language_string(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3624
        not counted in Rate Limit.
        """
        url = '{}{}/{}/language-string'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def languages(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3631
        not counted to rate limit
        """
        url = '{}{}/{}/languages'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def maps(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3635
        not counted to rate limit
        """
        url = '{}{}/{}/map'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def mastery_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3625
        not counted to rate limit
        """
        url = '{}{}/{}/mastery'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def mastery(self, mastery_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3626
        not counted to rate limit
        """
        url = '{}{}/{}/mastery/{}'.format(api_url, region, version, mastery_id)
        return self._get_data(url, kwargs)

    def realm(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3632
        not counted to rate limit
        """
        url = '{}{}/{}/realm'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def rune_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3623
        not counted to rate limit
        """
        url = '{}{}/{}/rune'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def rune(self, rune_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3629
        not counted to rate limit
        """
        url = '{}{}/{}/rune/{}'.format(api_url, region, version, rune_id)
        return self._get_data(url, kwargs)

    def summoner_spell_all(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3634
        not counted to rate limit
        """
        url = '{}{}/{}/summoner-spell'.format(api_url, region, version)
        return self._get_data(url, kwargs)

    def summoner_spell(self, summoner_spell_id, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3628
        not counted to rate limit
        """
        url = '{}{}/{}/summoner-spell/{}'.format(api_url, region, version, summoner_spell_id)
        return self._get_data(url, kwargs)

    def versions(self, region=region_default, **kwargs):
        """
        https://developer.riotgames.com/api/methods#!/1055/3630
        not counted to rate limit
        """
        url = '{}{}/{}/versions'.format(api_url, region, version)
        return self._get_data(url, kwargs)
