import sys
import os

from requests import RequestException

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi.utils import check_response_code


def test_check_response_code():
    check_response_code(200)

    try:
        check_response_code(500)
    except RequestException:
        pass
    else:
        raise AssertionError
