# encoding: utf-8
import pytest

from lol_api.api.champion import champion, champions_all
from lol_api.data import api_versions
from lol_api._utils import get_region, get_data_from_api,  base_url

from tests.utils import BaseTestClass, initialize_settings, region_default


api_url = '{}/api/lol/eune/{}'.format(base_url, api_versions['champion'])
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()


class TestChampionsAll(BaseTestClass):
    control_url = '{}/champion'.format(api_url)

    @pytest.fixture
    def data(self):
        return champions_all()


class TestChampion(BaseTestClass):
    control_url = '{}/champion/1'.format(api_url)

    @pytest.fixture
    def data(self):
        return champion(champion_id=1)
