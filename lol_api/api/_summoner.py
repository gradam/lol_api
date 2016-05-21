# encoding: utf-8
from lol_api._base_api_class import BaseApiClass
from lol_api._utils import count_request, to_comma_separated, base_url
from lol_api.data import api_versions

version = api_versions['summoner']
api_url = '{}/api/lol/'.format(base_url)


class Summoner(BaseApiClass):

    @count_request
    def by_name(self, summoner_names, region=None, **kwargs):
        """
        Get summoner objects mapped by standardized summoner name for a given list of summoner names.
        https://developer.riotgames.com/api/methods#!/1079/3722
        :param  summoner_names: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        names = to_comma_separated(summoner_names)
        url = '{}{}/{}/summoner/by-name/{}'.format(api_url, region, version, names)
        return self._get_data(url, **kwargs)

    @count_request
    def by_id(self, summoner_ids, region=None, **kwargs):
        """
        Get summoner objects mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3724
        :param summoner_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def masteries(self, summoner_ids, region=None, **kwargs):
        """
        Get mastery pages mapped by summoner ID for a given list of summoner IDs
        https://developer.riotgames.com/api/methods#!/1079/3723
        :param summoner_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/masteries'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def name(self, summoner_ids, region=None, **kwargs):
        """
        Get summoner names mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3720
        :param summoner_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/name'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def runes(self, summoner_ids, region=None, **kwargs):
        """
        Get rune pages mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3719
        :param summoner_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/runes'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)