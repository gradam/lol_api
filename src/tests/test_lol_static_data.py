# encoding: utf-8
import pytest

from riotApi import Client
from riotApi._utils import base_url, api_versions, region_default
from tests.utils import test_api_key, BaseTestClass


static_api = Client(test_api_key, unlimited=True).LolStaticData
version = api_versions['lol-static-data']
api_url = '{}/api/lol/static-data/{}/{}'.format(base_url, region_default, version)


class TestChampionsAll(BaseTestClass):
    control_url = '{}/champion'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.champions_all(champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'


class TestChampion(BaseTestClass):
    control_url = '{}/champion/1'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.champion(champ_id=1, champData='all')

    def test_params(self, data):
        assert self.request_params['champData'] == 'all'


class TestItemsAll(BaseTestClass):
    control_url = '{}/item'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.items_all(itemListData='all')

    def test_params(self, data):
        assert self.request_params['itemListData'] == 'all'


class TestItem(BaseTestClass):
    control_url = '{}/item/1'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.item(item_id=1, itemListData='all')

    def test_params(self, data):
        assert self.request_params['itemListData'] == 'all'


class TestLanguageString(BaseTestClass):
    control_url = '{}/language-string'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.language_string(locale='pl_PL')

    def test_params(self, data):
        assert self.request_params['locale'] == 'pl_PL'


class Test(BaseTestClass):
    control_url = '{}/languages'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.languages()


class TestMaps(BaseTestClass):
    control_url = '{}/map'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.maps(version='6.4')

    def test_params(self, data):
        assert self.request_params['version'] == '6.4'


class TestMasteryAll(BaseTestClass):
    control_url = '{}/mastery'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.mastery_all(masteryListData='all')

    def test_params(self, data):
        assert self.request_params['masteryListData'] == 'all'


class TestMastery(BaseTestClass):
    control_url = '{}/mastery/1'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.mastery(mastery_id=1, masteryListData='all')

    def test_params(self, data):
        assert self.request_params['masteryListData'] == 'all'


class TestRealm(BaseTestClass):
    control_url = '{}/realm'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.realm()


class TestRuneAll(BaseTestClass):
    control_url = '{}/rune'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.rune_all(runeListData='all')

    def test_params(self, data):
        assert self.request_params['runeListData'] == 'all'


class TestRune(BaseTestClass):
    control_url = '{}/rune/1'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.rune(rune_id=1, runeListData='all')

    def test_params(self, data):
        assert self.request_params['runeListData'] == 'all'


class TestSummonerSpellAll(BaseTestClass):
    control_url = '{}/summoner-spell'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.summoner_spell_all(spelldata='cooldown')

    def test_params(self, data):
        assert self.request_params['spelldata'] == 'cooldown'


class TestSummonerSpell(BaseTestClass):
    control_url = '{}/summoner-spell/22'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.summoner_spell(summoner_spell_id=22, spelldata='cooldown')

    def test_params(self, data):
        assert self.request_params['spelldata'] == 'cooldown'


class TestVersions(BaseTestClass):
    control_url = '{}/versions'.format(api_url)

    @pytest.fixture()
    def data(self):
        return static_api.versions()
