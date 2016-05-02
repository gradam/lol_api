# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import region_default, base_url, api_versions, count_request

version = api_versions['match']
api_url = '{}/api/lol/'.format(base_url)


class Match(BaseApiClass):

    @count_request
    def match(self, match_id, region=region_default, **kwargs):
        """
        Retrieve match by match ID.
        https://developer.riotgames.com/api/methods#!/1064/3671
        """
        url = '{}{}/{}/match/{}'.format(api_url, region, version, match_id)
        return self._get_data(url, **kwargs)



