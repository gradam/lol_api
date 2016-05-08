It is python wrapper for League of Legends api that watch out to not
exceed rate limit.

Tested on **python 3.5** and **python 2.7.11**

Full api documentation:
`link <https://developer.riotgames.com/api/methods>`__


Installation:
=============
Package is available on PyPI so just use:

``pip install lol_api``

or to install from source:

``git clone https://github.com/gradam/lol_api.git``

``python setup.py test``

``python setup.py install``

Usage:
======

To start using api simple import lol\_api and then create Client object
and pass as arguments api\_key and default region to use when no other
specified in api call. eg.

.. code:: python

    from lol_api import Client
    client = Client('my_api_key', 'eune')

Structure of a class correspond to Riot's documentation. So to get
information about summoner by name:

.. code:: python

    client.Summoner.by_name('my_name')

Each method returns data in form of dictionary

Extra arguments:
================

To specify the region pass ``region='your_region'`` as argument to
method, if not specified ``region_default`` passed to Client will be
used.

If lol api accept optional arguments, it should be pass as a keyword
named exactly as expected by api. eg.

.. code:: python

    client.LolStaticData.champion(champData='all')

Additional Data:
================

``lol_api.data``
----------------

-  ``error_codes`` - Explain error codes that you can get from requests
-  ``regions`` - map region names to shortcuts
-  ``platforms`` - map region shortcuts to platform name
-  ``queue_types`` - map queue names to short descriptions
-  ``api_versions`` - map APIs to versions

Rate limit:
===========

Wrapper automatically watch to no exceed requests rate limit per region.
Default value is 10 per 10 seconds and 500 per 10 minutes. This is
default `limit <https://developer.riotgames.com/docs/api-keys>`__ for
non production keys. Id order to use production limit ( 3000 per 10
seconds and 180000 per 10 minutes ) pass ``production=True`` to Client:

.. code:: python

    client = Client('api_key', 'euw', production=True)

You can also turn this off by passing ``unlimited=True`` to Client.

**If Rate limit is exceeded
``lol_api.exceptions.RateLimitExceededError`` will be raised.**

Running tests
=============

Requirements for tests are in tests\_requirements.txt file.

To run test go to ``tests`` directory and run:

``py.test``

or better run:
``python setup.py test``

TODO:
=====

-  Better documentation
-  Add possibility to cache responses
-  Add inplace translation champion name to id
-  Queue for requests when limit exceeded
