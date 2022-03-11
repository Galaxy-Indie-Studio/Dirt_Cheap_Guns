import time
import sys
from gis.dirt_cheap_guns.gun_websites import cheaper_than_dirt
from gis.dirt_cheap_guns.ammo_websites import bulk_cheap_ammo
from gis.dirt_cheap_guns.utils import keyword_search
from gis.dirt_cheap_guns.utils import update_program


def search_all_gun_sites():
    cheaper_than_dirt_url = "https://www.cheaperthandirt.com/"

    print(f"Searching {cheaper_than_dirt_url}.....")
    print('')
    cheaper_than_dirt.search_site('https://www.cheaperthandirt.com/firearms/handguns/',
                                  'https://www.cheaperthandirt.com/firearms/shotguns/',
                                  'https://www.cheaperthandirt.com/firearms/rifles/',
                                  'https://www.cheaperthandirt.com/firearms/tactical/')
    print(f"Finished searching {cheaper_than_dirt_url}!")
    print('')

def search_all_ammo_sites():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url}.....")
    print('')
    bulk_cheap_ammo.search_site('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=290',   # 12 Gauge
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=292',   # 16 Guage
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=294',   # 20 Gauge
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=304',   # 410 Bore
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=52',    # 9mm
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=210',   # 5.56x45mm Nato
                                'https://www.bulkcheapammo.com/bulk-ammo?calibers[]=243')   # 7.62x39mm
    print(f"Finished searching {bulk_cheap_ammo_url}!")
    print('')


if __name__ == '__main__':
    update_site= 'https://galaxy-indie-studio.github.io/Galaxy-Indie-Studio-Website/programs.html'
    version = 'Alpha 1.0.0'

    while True:
        update_program.check_updates(update_site, version)

        keyword_search.search_keyword()


