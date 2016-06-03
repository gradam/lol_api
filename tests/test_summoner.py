# encoding: utf-8
import pytest


from lol_api.api.summoner import *
from lol_api.data import api_versions
from lol_api.utils import base_url
from tests.utils import initialize_settings, region_default, BaseTestClass


version = api_versions['summoner']
api_url = '{}/api/lol/{}/{}/summoner/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()

class TestByName(BaseTestClass):
    control_url = '{}by-name/test name1,name 2'.format(api_url)

    @pytest.fixture
    def data(self):
        return by_name(['test name1', 'name 2'])


class TestById(BaseTestClass):
    control_url = '{}333,444'.format(api_url)

    @pytest.fixture
    def data(self):
        return by_id([333, 444])


class TestMasteries(BaseTestClass):
    control_url = '{}123/masteries'.format(api_url)

    @pytest.fixture
    def data(self):
        return masteries(123)


class TestName(BaseTestClass):
    control_url = '{}333,444/name'.format(api_url)

    @pytest.fixture
    def data(self):
        return name([333, 444])


class TestRunes(BaseTestClass):
    control_url = '{}333,444/runes'.format(api_url)

    @pytest.fixture
    def data(self):
        return runes([333, 444])
