# encoding: utf-8
import sys
import os
import json

import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi._utils import base_url
from riotApi._lol_static_data import LolStaticData

from riotApi.tests.utils import MockRequest

static_api = LolStaticData('test_key')

test_json = {'3': "bb", "a": 4}


class BaseTestClass:
    control_url = ''

    @pytest.fixture(autouse=True)
    def mock_request_get(self, monkeypatch):
        monkeypatch.setattr(requests, 'get', self.get_mock_func)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.request_params = {}
        self.mock_request = MockRequest(test_json)

    def get_mock_func(self, url, **kwargs):
        self.requested_url = url
        self.request_params = (kwargs['params'])
        return self.mock_request

    def test_api_key(self, data):
        assert self.request_params['api_key'] == static_api.api_key

    def test_response_data(self, data):
        assert data == test_json

    def test_requested_url(self, data):
        assert self.requested_url == self.control_url


class TestChampionsAll(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/champion'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.champions_all(champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'


class TestChampion(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/champion/1'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.champion(champ_id=1, champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'


class TestItemsAll(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/item'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.items_all(itemListData='all')

    def test_params(self, data):
        assert self.request_params['itemListData'] == 'all'


class TestItem(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/item/1'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.item(item_id=1, itemListData='all')

    def test_params(self, data):
        assert self.request_params['itemListData'] == 'all'


class TestLanguageString(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/language-string'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.language_string(locale='pl_PL')

    def test_params(self, data):
        assert self.request_params['locale'] == 'pl_PL'


class Test(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/languages'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.languages()


class TestMaps(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/map'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.maps(version='6.4')

    def test_params(self, data):
        assert self.request_params['version'] == '6.4'


class TestMasteryAll(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/mastery'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.mastery_all(masteryListData='all')

    def test_params(self, data):
        assert self.request_params['masteryListData'] == 'all'


class TestMastery(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/mastery/1'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.mastery(mastery_id=1, masteryListData='all')

    def test_params(self, data):
        assert self.request_params['masteryListData'] == 'all'


class TestRealm(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/realm'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.realm()


class TestRuneAll(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/rune'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.rune_all(runeListData='all')

    def test_params(self, data):
        assert self.request_params['runeListData'] == 'all'


class TestRune(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/rune/1'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.rune(rune_id=1, runeListData='all')

    def test_params(self, data):
        assert self.request_params['runeListData'] == 'all'


class TestSummonerSpellAll(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/summoner-spell'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.summoner_spell_all(spelldata='cooldown')

    def test_params(self, data):
        assert self.request_params['spelldata'] == 'cooldown'


class TestSummonerSpell(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/summoner-spell/22'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.summoner_spell(summoner_spell_id=22, spelldata='cooldown')

    def test_params(self, data):
        assert self.request_params['spelldata'] == 'cooldown'


class TestVersions(BaseTestClass):
    control_url = '{}/api/lol/static-data/eune/v1.2/versions'.format(base_url)

    @pytest.fixture()
    def data(self):
        return static_api.versions()
