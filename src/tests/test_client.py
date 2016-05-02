# encoding: utf-8
from riotApi._api_client import Client
from riotApi._local_data import LocalData
from riotApi._lol_static_data import LolStaticData
from riotApi._utils import RateLimitWatcher


def test_object_create():
    c = Client('test_api_key')
    assert c.api_key == 'test_api_key'
    assert isinstance(c.watcher, RateLimitWatcher)
    assert isinstance(c.LolStaticData, LolStaticData)
    assert isinstance(c.LocalData, LocalData)