# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, to_comma_separated, base_url
from riotApi.data import api_versions

version = api_versions['league']
api_url = '{}/api/lol/'.format(base_url)


class League(BaseApiClass):

    @count_request
    def by_summoners(self, summoner_ids, region=None, **kwargs):
        """
        Get leagues mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/985/3351
        :param summoner_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/league/by-summoner/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def by_summoners_entry(self, summoner_ids, region=None, **kwargs):
        """
        Get league entries mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/985/3356
        :param summoner_ids: can be both list or string in valid formats
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/league/by-summoner/{}/entry'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def by_teams(self, team_ids, region=None, **kwargs):
        """
        Get leagues mapped by team ID for a given list of team IDs.
        https://developer.riotgames.com/api/methods#!/985/3352
        :param team_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(team_ids)
        url = '{}{}/{}/league/by-team/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def by_teams_entry(self, team_ids, region=None, **kwargs):
        """
        Get league entries mapped by team ID for a given list of team IDs.
        https://developer.riotgames.com/api/methods#!/985/3355
        :param team_ids: can be both list or string in valid format
        """
        region = self._region_to_valid(region)
        ids = to_comma_separated(team_ids)
        url = '{}{}/{}/league/by-team/{}/entry'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def challenger(self, region=None, **kwargs):
        """
        Get challenger tier leagues.
        https://developer.riotgames.com/api/methods#!/985/3353
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/league/challenger'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    @count_request
    def master(self, region=None, **kwargs):
        """
        Get master tier leagues.
        https://developer.riotgames.com/api/methods#!/985/3354
        """
        region = self._region_to_valid(region)
        url = '{}{}/{}/league/master'.format(api_url, region, version)
        return self._get_data(url, **kwargs)
