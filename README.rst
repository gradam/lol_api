It is python wrapper for League of Legends api that watch out to not
exceed rate limit.

Tested on **python 3.5**

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

First you need to set up few thing. To do so import settings.

.. code:: python

    from lol_api.settings import settings
    settings.API_KEY = 'your_api_key'
    # If you do not wont to pass region to each api call just do:
    settings.REGION_DEFAULT = 'some_region'
    # Now if you are going to use watcher daemon you have to pass server info:
    settings.DAEMON_SERVER = ('server_ip', port)
    # If you prefer to use local watcher instance
    settings.initialize_watcher()

Example:
--------

.. code:: python

    from lol_api.settings import settings
    from lol_api.api.champion import champion

    settings.API_KEY = 'mysecretapikey123'
    settings.REGION_DEFAULT = 'eune'
    settings.initialie_watcher(production=True)

    data = champion(champion_id=2)


Daemon:
=======

To use Daemon for watching request count run him in another python instance.

.. code:: python

    from lol_api.daemon import ApiDaemon
    daemon = ApiDaemon()
    daemon.run()


Additional arguments:

- ``port`` - Port to run on. Default(8877)
- ``host`` - Host for socketserver.ThreadingTCPServer. Default('localhost')
- ``production`` - set requests limit for production limits. Default(False)
- ``unlimited`` - do not count requests. Default(False)
- ``log`` - printout information about inquiry. Default(True)




Extra arguments:
================

To specify the region pass ``region='your_region'`` as the argument to
method, if not specified ``region_default`` passed to Client will be
used.

If lol api accept optional arguments, it should be pass as a keyword
named exactly as expected by api. eg.

.. code:: python

    lol_api.api.lol_static_data.champion(champData='all')

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

Wrapper automatically watch to not exceed requests rate limit per region.
Default value is 10 per 10 seconds and 500 per 10 minutes. This is
default `limit <https://developer.riotgames.com/docs/api-keys>`__ for
non production keys. Id order to use production limit ( 3000 per 10
seconds and 180000 per 10 minutes ) set PRODUCTION to True in settings.

.. code:: python

    lol_api.settings.settings.PRODUCTION = True

You can also turn this off by setting ``UNLIMITED=True``.

**If Rate limit is exceeded
``lol_api.exceptions.RateLimitExceededError`` will be raised.**

Running tests
=============

Requirements for tests are in tests\_requirements.txt file.

To run tests:

``pip install -r tests_requirements.txt``

``py.test``

or run:

``python setup.py test``

TODO:
=====

-  Better documentation
-  Add possibility to cache responses
-  Add inplace translation champion name to id
-  Queue for requests when limit exceeded
