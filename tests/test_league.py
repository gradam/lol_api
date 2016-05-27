# encoding: utf-8
import pytest

from lol_api.client import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass

region_default = 'eune'

league = Client(test_api_key, region_default, unlimited=True).League

version = api_versions['league']
api_url = '{}/api/lol/{}/{}/league/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


class TestBySummoners(BaseTestClass):
    control_url = '{}by-summoner/123,111'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.by_summoners([123, 111])

    def test_with_string(self):
        test_url = '{}by-summoner/123,222'.format(api_url)
        league.by_summoners('123,222')
        assert self.requested_url == test_url


class TestBySummonersEntry(BaseTestClass):
    control_url = '{}by-summoner/123,111/entry'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.by_summoners_entry([123, 111])

    def test_with_string(self):
        test_url = '{}by-summoner/123,222/entry'.format(api_url)
        league.by_summoners_entry('123,222')
        assert self.requested_url == test_url


class TestByTeams(BaseTestClass):
    control_url = '{}by-team/123,111'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.by_teams([123, 111])

    def test_with_string(self):
        test_url = '{}by-team/123,222'.format(api_url)
        league.by_teams('123,222')
        assert self.requested_url == test_url


class TestByTeamsEntry(BaseTestClass):
    control_url = '{}by-team/123,111/entry'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.by_teams_entry([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/las/{}/league/by-team/123,222/entry'.format(base_url, version)
        test_url = test_url.format('las')
        league.by_teams_entry('123,222', region='las')
        assert self.requested_url == test_url


class TestChallenger(BaseTestClass):
    control_url = '{}challenger'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.challenger()


class TestMaster(BaseTestClass):
    control_url = '{}master'.format(api_url)

    @pytest.fixture
    def data(self):
        return league.master()

