# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions, count_request, to_comma_separated
from riotApi._base_api_class import BaseApiClass

version = api_versions['summoner']
api_url = '{}/api/lol/'.format(base_url)


class Summoner(BaseApiClass):

    @count_request
    def by_name(self, summoner_names, region=region_default, **kwargs):
        """
        Get summoner objects mapped by standardized summoner name for a given list of summoner names.
        https://developer.riotgames.com/api/methods#!/1079/3722
        """
        names = to_comma_separated(summoner_names)
        url = '{}{}/{}/summoner/by-name/{}'.format(api_url, region, version, names)
        return self._get_data(url, **kwargs)

    @count_request
    def by_id(self, summoner_ids, region=region_default, **kwargs):
        """
        Get summoner objects mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3724
        """
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def masteries(self, summoner_ids, region=region_default, **kwargs):
        """
        Get mastery pages mapped by summoner ID for a given list of summoner IDs
        https://developer.riotgames.com/api/methods#!/1079/3723
        """
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/masteries'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def name(self, summoner_ids, region=region_default, **kwargs):
        """
        Get summoner names mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3720
        """
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/name'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def runes(self, summoner_ids, region=region_default, **kwargs):
        """
        Get rune pages mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/1079/3719
        """
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/summoner/{}/runes'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)
