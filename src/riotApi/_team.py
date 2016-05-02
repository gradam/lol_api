# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions, count_request, to_comma_separated
from riotApi._base_api_class import BaseApiClass

version = api_versions['team']
api_url = '{}/api/lol/'.format(base_url)


class Team(BaseApiClass):

    @count_request
    def by_summoners(self, summoner_ids, region=region_default, **kwargs):
        """
        Get teams mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/986/3358
        """
        ids = to_comma_separated(summoner_ids)
        url = '{}{}/{}/team/by-summoner/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    @count_request
    def by_teams(self, team_ids, region=region_default, **kwargs):
        """
        Get teams mapped by team ID for a given list of team IDs.
        https://developer.riotgames.com/api/methods#!/986/3357
        """
        ids = to_comma_separated(team_ids)
        url = '{}{}/{}/team/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)
