# encoding: utf-8
import pytest

from lol_api.api.stats import *
from lol_api.data import api_versions
from lol_api.utils import base_url
from tests.utils import region_default, initialize_settings, BaseTestClass


version = api_versions['stats']
api_url = '{}/api/lol/{}/{}/stats/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()

class TestRanked(BaseTestClass):
    control_url = '{}by-summoner/123/ranked'.format(api_url)

    @pytest.fixture
    def data(self):
        return ranked(123)


class TestSummary(BaseTestClass):
    control_url = '{}by-summoner/123/summary'.format(api_url)

    @pytest.fixture
    def data(self):
        return summary(123)
