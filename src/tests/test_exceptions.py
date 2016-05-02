# encoding: utf-8
import pytest

from riotApi.exceptions import RateLimitExceededError


def test_message():
    with pytest.raises(RateLimitExceededError) as error:
        raise RateLimitExceededError
    assert 'Requests rate limit exceeded' == str(error.value)
