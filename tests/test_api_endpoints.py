from wargaming import *


def test_endpoints():
    region_map = [
        ('ru', 'ru'),
        ('en', 'asia'),
        ('en', 'na'),
        ('en', 'eu'),
    ]

    for game in [WoT, WoTB, WoWS, WoWP]:
        for region in region_map:
            if game == WoWP and region[1] == 'asia':
                continue
            print("%-20s %4s %s" % (
                game, region[1], repr(game('demo', *region).account.list(search='alex'))[0:80]))

    for region in [('en', 'ps4'), ('en', 'xbox')]:
        print("%-20s %4s %s" % (WoTX, region[1],
                                repr(WoTX('demo', *region).account.list(search='alex'))[0:80]))
