# encoding: utf-8


class RateLimitExceededError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'Requests rate limit exceeded', *args, **kwargs)
