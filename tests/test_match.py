# encoding: utf-8
import pytest

from lol_api import Client
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import test_api_key, BaseTestClass


region_default = 'eune'
match = Client(test_api_key, region_default, unlimited=True).Match

version = api_versions['match']
api_url = '{}/api/lol/{}/{}/match/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


class TestMatch(BaseTestClass):
    control_url = '{}123'.format(api_url)

    @pytest.fixture
    def data(self):
        return match.match(123)
