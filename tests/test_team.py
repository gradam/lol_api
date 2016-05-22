# encoding: utf-8
import pytest

from lol_api import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass


region_default = 'euw'
team = Client(test_api_key, 'euw', unlimited=True).Team

version = api_versions['team']
api_url = '{}/api/lol/{}/{}/team/'.format(base_url, region_default, version)


class TestBySummoners(BaseTestClass):
    control_url = '{}by-summoner/333,222'.format(api_url)

    @pytest.fixture
    def data(self):
        return team.by_summoners([333, 222])


class TestByTeams(BaseTestClass):
    control_url = '{}123,456'.format(api_url)

    @pytest.fixture
    def data(self):
        return team.by_teams('123,456')
