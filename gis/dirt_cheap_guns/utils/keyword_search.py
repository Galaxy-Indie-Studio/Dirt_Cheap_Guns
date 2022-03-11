from gis.dirt_cheap_guns.ammo_websites import bulk_cheap_ammo
from gis.dirt_cheap_guns.gun_websites import cheaper_than_dirt
import time
import sys


def search_keyword():
    time_wait = 1
    searching = True

    while searching:
        print('Would you like to search for Guns, Ammo or Both')
        user_input = input("> ")

        if 'guns' in user_input:
            gun_true = True
            while gun_true:
                # search_all_gun_sites()
                a = 1

                while a == 1:
                    print(f"Would you like to continue to run the program or go back to search! This program "
                          f"updates every {time_wait} minutes!")
                    user_input = input('> ')

                    if 'yes' in user_input:
                        print(f'Waiting for {time_wait} minutes...')
                        time.sleep(time_wait * 60)
                        a = 0
                    if 'no' in user_input:
                        a = 0
                        gun_true = False

        if 'ammo' in user_input:
            search_ammo = True

            while search_ammo:
                print('What caliber of ammo would you like to find? Type Any for all Ammo')
                user_input_two = input('> ')
                search_caliber = True
                while search_caliber:
                    if '12 gauge' in user_input_two:
                        find_12_gauge_ammo()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber = False
                                update = False
                    elif '16 gauge' in user_input_two:
                        find_16_gauge_ammo()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '20 gauge' in user_input_two:
                        find_20_gauge_ammo()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '410 bore' in user_input_two:
                        find_410_bore_ammo()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '.22 lr' in user_input_two:
                        find_22_lr()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '9mm' in user_input_two:
                        find_9mm()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '5.56x45mm Nato' in user_input_two:
                        find_556_nato()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False
                    elif '7.62x39' in user_input_two:
                        find_762_mm()
                        update = True

                        while update:
                            print(f"Would you like to continue to run the program or go back to search! This program "
                                  f"updates every {time_wait} minutes")
                            user_input = input('> ')

                            if 'yes' in user_input:
                                print(f'Waiting for {time_wait} minutes...')
                                time.sleep(time_wait * 60)
                                update = False
                            if 'no' in user_input:
                                search_caliber= False
                                update = False


def find_12_gauge_ammo():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 12 Gauge Shells.....")
    print('')
    bulk_cheap_ammo.find_12_gauge('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=290')
    print(f"Finished searching {bulk_cheap_ammo_url} for 12 Gauge Shells!")
    print('')


def find_16_gauge_ammo():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 16 Gauge Shells.....")
    print('')
    bulk_cheap_ammo.find_16_gauge('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=292')
    print(f"Finished searching {bulk_cheap_ammo_url} for 16 Gauge Shells!")
    print('')


def find_20_gauge_ammo():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 20 Gauge Shells.....")
    print('')
    bulk_cheap_ammo.find_20_gauge('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=294')
    print(f"Finished searching {bulk_cheap_ammo_url} for 20 Gauge Shells!")
    print('')


def find_410_bore_ammo():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 410 Bore.....")
    print('')
    bulk_cheap_ammo.find_410('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=304')
    print(f"Finished searching {bulk_cheap_ammo_url} for 410 Bore!")
    print('')


def find_22_lr():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for .22 lr.....")
    print('')
    bulk_cheap_ammo.find_22_lr('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=83')
    print(f"Finished searching {bulk_cheap_ammo_url} for .22 lr!")
    print('')


def find_9mm():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 9mm ammo.....")
    print('')
    bulk_cheap_ammo.find_9mm('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=52')
    print(f"Finished searching {bulk_cheap_ammo_url} for 9mm ammo!")
    print('')


def find_556_nato():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'

    print(f"Searching {bulk_cheap_ammo_url} for 5.56x45mm Nato.....")
    print('')
    bulk_cheap_ammo.find_556_nato('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=210')
    print(f"Finished searching {bulk_cheap_ammo_url} for 5.56x45mm Nato!")
    print('')


def find_762_mm():
    bulk_cheap_ammo_url = 'https://www.bulkcheapammo.com/'
    print(f"Searching {bulk_cheap_ammo_url} for 7.62x39mm.....")
    print('')
    bulk_cheap_ammo.find_762_mm('https://www.bulkcheapammo.com/bulk-ammo?calibers[]=243')
    print(f"Finished searching {bulk_cheap_ammo_url} for 7.62x39mm!")
    print('')


