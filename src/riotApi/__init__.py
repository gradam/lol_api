# encoding: utf-8
from . import utils
from collections import defaultdict


api_key = utils.get_api_key()

region_default = 'eune'

error_codes = defaultdict(lambda: 'Unknown error code',)
error_codes.update({
    400: 'Bad request',
    401: 'Unauthorized',
    404: 'Data not found',
    429: 'Rate limit exceeded',
    500: 'Internal server error',
    503: 'Service unavailable',
})

base_url = 'https://global.api.pvp.net'
