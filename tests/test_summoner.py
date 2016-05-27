# encoding: utf-8
import pytest

from lol_api.client import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass


region_default = 'euw'
summoner = Client(test_api_key, region_default, unlimited=True).Summoner

version = api_versions['summoner']
api_url = '{}/api/lol/{}/{}/summoner/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


class TestByName(BaseTestClass):
    control_url = '{}by-name/test name1,name 2'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.by_name(['test name1', 'name 2'])


class TestById(BaseTestClass):
    control_url = '{}333,444'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.by_id([333, 444])


class TestMasteries(BaseTestClass):
    control_url = '{}123/masteries'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.masteries(123)


class TestName(BaseTestClass):
    control_url = '{}333,444/name'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.name([333, 444])


class TestRunes(BaseTestClass):
    control_url = '{}333,444/runes'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.runes([333, 444])
