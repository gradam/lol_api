# encoding: utf-8


class RateLimitExceededError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'Requests rate limit exceeded', *args, **kwargs)


class InvalidRegionError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'Given region is Invalid', *args, **kwargs)


class NoApiKeySpecified(Exception):
    def __init__(self, *args, **kwargs):
        massage = 'Api Key not Specified in environment variable' \
                  ' neither in global settings or Client object'
        Exception.__init__(self, massage, *args, **kwargs)


class RegionDefaultNotSpecified(Exception):
    def __init__(self, *args, **kwargs):
        massage = 'Default region not specified in global settings neither in Client object'
        Exception.__init__(self, massage, *args, **kwargs)
