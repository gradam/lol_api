# encoding: utf-8
import os
from collections import defaultdict

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

with open(os.path.join(os.path.dirname(__file__), 'api_key.txt'), 'r') as key_file:
    api_key = key_file.readline()
