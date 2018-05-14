Python library for Wargaming.net API
====================================

Pure pythonic library for accessing Wargaming.net API (https://wargaming.net/developers/).

Compatible with a Python>=2.7 and Python >=3.4 versions. PyPy also!

.. image:: https://travis-ci.org/svartalf/python-wargaming.svg?branch=master
.. image:: https://readthedocs.org/projects/python-wargaming/badge/?version=latest
.. image:: https://badge.fury.io/py/wargaming.svg

Installation
------------

As simple as usual:

    $ pip install wargaming


Usage
-----

.. code:: python

    import wargaming
    
    API_KEY = 'demo'
    
    wgn = wargaming.WGN(API_KEY, region='ru', language='ru')
    wot = wargaming.WoT(API_KEY, region='ru', language='ru')
    serb = wgn.account.list(search='SerB')[0]  # well known person in WG
    
    tank_names = {int(k): v for k, v in wot.encyclopedia.tanks(fields=['name_i18n']).items()}
    
    print('Tanks statistics:\n%-40s : %s' % ('Tank name', 'Win Rate'))
    for tank in wot.account.tanks(account_id=serb['account_id'])[str(serb['account_id'])]:
        name = tank_names.get(tank['tank_id'], {}).get('name_i18n') or 'No such vehicle in encyclopedia'
        wins = tank['statistics']['wins']
        battles = tank['statistics']['battles']
        win_rate = 100.0 * wins / battles
        print('%-40s : %.2f%% (%s / %s)' % (name, win_rate, wins, battles))


Documentation
-------------

Wargaming.NET API documentation: https://na.wargaming.net/developers/api_reference/

Library documentation: http://python-wargaming.rtfd.org

Supported WGAPI
---------------

 * World of Tanks
 * World of Warplanes
 * World of Warships
 * World of Tanks Blitz
 * Wargaming.NET common API

Contribution
------------

Just fork, update and send pull request. Do not forget to run tests:

    $ tox

Also check for a PEP-0008 compliance:

    $ pep8 --max-line-length=120 wargaming

Contributors
------------

 * monester
 * LanceMaverick
