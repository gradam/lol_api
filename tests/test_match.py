# encoding: utf-8
import pytest

from lol_api.api.match import *
from lol_api.data import api_versions
from lol_api._utils import base_url
from tests.utils import region_default, initialize_settings, BaseTestClass


version = api_versions['match']
api_url = '{}/api/lol/{}/{}/match/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()


class TestMatch(BaseTestClass):
    control_url = '{}123'.format(api_url)

    @pytest.fixture
    def data(self):
        return match(123)
