# encoding: utf-8
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi.championsID import get_champion_info


def test_champions_info_instances():
    champ = get_champion_info('darius')
    assert isinstance(champ.ID, int)
    assert isinstance(champ.name, str)


def test_champions_search_by_name():
    champ = get_champion_info('darius')
    assert champ.name == 'darius'
    assert champ.ID == 122


def test_champions_search_by_id():
    champ = get_champion_info(432)
    assert champ.name == 'bard'
    assert champ.ID == 432
