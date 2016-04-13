import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi.utils import check_response_code


def test_check_response_code():
    check_response_code(200)

    with pytest.raises(Exception) as e_info:
        check_response_code(500)
