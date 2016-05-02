It is python wrapper for League of Legends api

Full api documentation: [link](https://developer.riotgames.com/api/methods)

# Usage:
To start using api simple import riotApi and then create Client object
```python
from riotApi import Client
client = Client('my_api_key')
```
Structure of a class correspond to Riot's documentation.
So to get information about summoner by name:
```python
client.Summoner.by_name('my_name')
```

Each method returns data in form of dictionary

# Extra arguments:
To specify the region pass `region='your_region'` as argument to method, if not specified `data.region_default` will be used.

If lol api accept optional arguments, it should be pass as a keyword named exactly as expected by api. eg.
```python
client.LolStaticData.champion(champData='all')
```


# Additional Data:
##  `riotApi.data`
`error_codes` - Explain error codes that you can get from requests

`regions` - map region names to shortcuts

`region_default` - region that will be used if no other given

`platforms` - map region shortcuts to platform name

`queue_types` - map queue names to short descriptions

`api_versions` - map APIs to versions


# Rate limit:
Wrapper automatically watch to no exceed requests rate limit. Default value is 10 per 10 seconds and 500 per 10 minutes.
This is default [limit](https://developer.riotgames.com/docs/api-keys) for non production keys.
Id order to use production limit ( 3000 per 10 seconds and 180000 per 10 minutes ) pass `production=True` to Client:
```python
client = Client('api_key', production=True) 
```
You can also turn this off by passing `unlimited=True` to Client.

**If Rate limit is exceeded `riotApi.exceptions.RateLimitExceededError` will be raised.**

# Running tests
Requirements for tests are in tests_requirements.txt file.

To run test go to `src` or `tests` directory and run:

`py.test`


# TODO:
Add possibility to cache responses

Add inplace translation champion name to id

Add different watchers for different regions
