# encoding: utf-8
import pytest

from lol_api.api.game import *
from lol_api.data import api_versions
from lol_api.utils import base_url
from tests.utils import region_default, initialize_settings, BaseTestClass

version = api_versions['game']
api_url = '{}/api/lol/{}/{}/game/'.format(base_url, region_default, version)
api_url = api_url.format(region_default)


def setup_module(module):
    initialize_settings()


class TestRecent(BaseTestClass):
    control_url = '{}by-summoner/123/recent'.format(api_url)

    @pytest.fixture
    def data(self):
        return recent(123)
