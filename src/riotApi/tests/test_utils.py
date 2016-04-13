from unittest.mock import mock_open

from riotApi.utils import get_api_key


def test_get_api_key(mocker):
    m = mock_open(read_data='wow@api%key*wow')
    mocker.patch('builtins.open', m, create=True)
    assert get_api_key() == 'wow@api%key*wow'
