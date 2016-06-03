# encoding: utf-8
import pytest

from lol_api.api.team import *
from lol_api.data import api_versions
from lol_api.utils import get_region, get_data_from_api,  base_url
from tests.utils import BaseTestClass, initialize_settings, region_default


version = api_versions['team']
api_url = '{}/api/lol/{}/{}/team/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()


class TestBySummoners(BaseTestClass):
    control_url = '{}by-summoner/333,222'.format(api_url)

    @pytest.fixture
    def data(self):
        return by_summoners([333, 222])


class TestByTeams(BaseTestClass):
    control_url = '{}123,456'.format(api_url)

    @pytest.fixture
    def data(self):
        return by_teams('123,456')
