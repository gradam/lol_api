# encoding: utf-8
import pytest
from tests.utils import region_default, initialize_settings, BaseTestClass

from lol_api.api.lol_status import *


api_url = 'http://status.leagueoflegends.com/shards'


def setup_module(module):
    initialize_settings()


class TestShards(BaseTestClass):
    control_url = '{}'.format(api_url)

    @pytest.fixture
    def data(self):
        return shards()


class TestShardsRegion(BaseTestClass):
    control_url = '{}/{}'.format(api_url, region_default)

    @pytest.fixture
    def data(self):
        return shards_region()

