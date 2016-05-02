# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi import Client
from riotApi._utils import base_url, region_default

league = Client(test_api_key, unlimited=True).League


class TestBySummoners(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/by-summoner/123,111'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.by_summoners([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/{}/v2.5/league/by-summoner/123,222'.format(base_url, region_default)
        league.by_summoners('123,222')
        assert self.requested_url == test_url


class TestBySummonersEntry(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/by-summoner/123,111/entry'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.by_summoners_entry([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/{}/v2.5/league/by-summoner/123,222/entry'.format(base_url, region_default)
        league.by_summoners_entry('123,222')
        assert self.requested_url == test_url


class TestByTeams(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/by-team/123,111'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.by_teams([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/{}/v2.5/league/by-team/123,222'.format(base_url, region_default)
        league.by_teams('123,222')
        assert self.requested_url == test_url


class TestByTeamsEntry(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/by-team/123,111/entry'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.by_teams_entry([123, 111])

    def test_with_string(self):
        test_url = '{}/api/lol/las/v2.5/league/by-team/123,222/entry'.format(base_url)
        league.by_teams_entry('123,222', region='las')
        assert self.requested_url == test_url


class TestChallenger(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/challenger'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.challenger()


class TestMaster(BaseTestClass):
    control_url = '{}/api/lol/{}/v2.5/league/master'.format(base_url, region_default)

    @pytest.fixture
    def data(self):
        return league.master()

