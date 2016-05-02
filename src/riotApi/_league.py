# encoding: utf-8
from riotApi._utils import region_default, base_url, api_versions
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request

version = api_versions['league']
api_url = '{}/api/lol/'.format(base_url)


class League(BaseApiClass):

    @staticmethod
    def get_ids_string(ids):
        if isinstance(ids, str):
            return ids
        else:
            return ','.join([str(x) for x in ids])

    @count_request
    def by_summoners(self, summoner_ids, region=region_default, **kwargs):
        """
        Get leagues mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/985/3351
        :param summoner_ids: can be both list or string in valid format
        """
        ids = self.get_ids_string(summoner_ids)
        url = '{}{}/{}/league/by-summoner/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    def by_summoners_entry(self, summoner_ids, region=region_default, **kwargs):
        """
        Get league entries mapped by summoner ID for a given list of summoner IDs.
        https://developer.riotgames.com/api/methods#!/985/3356
        :param summoner_ids: can be both list or string in valid formats
        """
        ids = self.get_ids_string(summoner_ids)
        url = '{}{}/{}/league/by-summoner/{}/entry'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    def by_teams(self, team_ids, region=region_default, **kwargs):
        """
        Get leagues mapped by team ID for a given list of team IDs.
        https://developer.riotgames.com/api/methods#!/985/3352
        :param team_ids: can be both list or string in valid format
        """
        ids = self.get_ids_string(team_ids)
        url = '{}{}/{}/league/by-team/{}'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    def by_teams_entry(self, team_ids, region=region_default, **kwargs):
        """
        Get league entries mapped by team ID for a given list of team IDs.
        https://developer.riotgames.com/api/methods#!/985/3355
        :param team_ids: can be both list or string in valid format
        """
        ids = self.get_ids_string(team_ids)
        url = '{}{}/{}/league/by-team/{}/entry'.format(api_url, region, version, ids)
        return self._get_data(url, **kwargs)

    def challenger(self, region=region_default, **kwargs):
        """
        Get challenger tier leagues.
        https://developer.riotgames.com/api/methods#!/985/3353
        """
        url = '{}{}/{}/league/challenger'.format(api_url, region, version)
        return self._get_data(url, **kwargs)

    def master(self, region=region_default, **kwargs):
        """
        Get master tier leagues.
        https://developer.riotgames.com/api/methods#!/985/3354
        """
        url = '{}{}/{}/league/master'.format(api_url, region, version)
        return self._get_data(url, **kwargs)
