import sys
import os

from requests import RequestException

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi.utils import check_response_code, get_champion_info


def test_check_response_code():
    check_response_code(200)

    with pytest.raises(Exception) as e_info:
        check_response_code(500)


class TestGetChampionInfo:

    def test_champions_info_instances(self):
        champ = get_champion_info('darius')
        assert isinstance(champ.ID, int)
        assert isinstance(champ.name, str)

    def test_champions_search_by_name(self):
        champ = get_champion_info('darius')
        assert champ.name == 'darius'
        assert champ.ID == 122

    def test_champions_search_by_id(self):
        champ = get_champion_info(432)
        assert champ.name == 'bard'
        assert champ.ID == 432
