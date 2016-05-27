# encoding: utf-8
import os

from lol_api.client import Client

from tests.utils import test_api_key
from lol_api.settings import settings


def test_api_key_in_environment_variables():
    os.environ['LOL_API_KEY'] = test_api_key
    c = Client(region_default='eune')
    assert c.api_key == test_api_key
    del os.environ['LOL_API_KEY']


def test_api_key_in_settings():
    settings.API_KEY = test_api_key
    c = Client(region_default='eune')
    assert c.api_key == test_api_key

