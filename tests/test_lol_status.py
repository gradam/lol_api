# encoding: utf-8
import pytest

from riotApi._utils import region_default
from riotApi import Client

from tests.utils import test_api_key, BaseTestClass


lol_status = Client(test_api_key, unlimited=True).LolStatus
api_url = 'http://status.leagueoflegends.com/shards'


class TestShards(BaseTestClass):
    control_url = '{}'.format(api_url)

    @pytest.fixture
    def data(self):
        return lol_status.shards()

    def test_api_key(self, data):
        with pytest.raises(KeyError):
            key = self.request_params['api_key']


class TestShardsRegion(BaseTestClass):
    control_url = '{}/{}'.format(api_url, region_default)

    @pytest.fixture
    def data(self):
        return lol_status.shards_region()

    def test_api_key(self, data):
        with pytest.raises(KeyError):
            key = self.request_params['api_key']
