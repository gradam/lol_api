# encoding: utf-8
from riotApi._utils import region_default, base_url
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, platforms, get_champion_id

api_url = '{}/championmastery/location/'.format(base_url)


class ChampionMastery(BaseApiClass):
    @count_request
    def champion_master(self, player_id, champion, region=region_default, **kwargs):
        """
        Get a champion mastery by player id and champion id.
        https://developer.riotgames.com/api/methods#!/1071/3697
        """
        champion_id = get_champion_id(champion)
        platform = platforms[region]
        url = '{}{}/player/{}/champion/{}'.format(api_url, platform, player_id, champion_id)
        return self._get_data(url, kwargs)

    @count_request
    def champions_points(self, player_id, region=region_default, **kwargs):
        """
        Get all champion mastery entries.
        https://developer.riotgames.com/api/methods#!/1071/3696
        """
        platform = platforms[region]
        url = '{}{}/player/{}/champions'.format(api_url, platform, player_id)
        return self._get_data(url, kwargs)

    @count_request
    def score(self, player_id, region=region_default, **kwargs):
        """
        Get a player's total champion mastery score.
        https://developer.riotgames.com/api/methods#!/1071/3698
        """
        platform = platforms[region]
        url = '{}{}/player/{}/score'.format(api_url, platform, player_id)
        return self._get_data(url, kwargs)

    @count_request
    def top_champions(self, player_id, region=region_default, **kwargs):
        """
        Get specified number of top champion mastery entries
        https://developer.riotgames.com/api/methods#!/1071/3692
        """
        platform = platforms[region]
        url = '{}{}/player/{}/topchampions'.format(api_url, platform, player_id)
        return self._get_data(url, kwargs)

