from bs4 import BeautifulSoup
import requests


def handgun_listings(handgun_url):
    html_url = requests.get(handgun_url).text
    soup = BeautifulSoup(html_url, "lxml")
    handguns = soup.find_all('div', class_='col-6 col-md-4 outer-tiles product-impression')
    for handgun in handguns:
        handgun_name = handgun.find('span', class_='first-line d-lg-none').text
        handgun_price = handgun.find('span', class_='sales').text
        handgun_desc = handgun.find('div', class_='pdp-link')
        handgun_desc_url = handgun_desc.a['href']

        print(f"-----------------------------------------------------------")
        print(f"Gun Name: {handgun_name}")
        print(f"{handgun_price}")
        print(f"For more info about this handgun, Visit {handgun_desc_url}")
        print(f"-----------------------------------------------------------")


def shotgun_listings(shotgun_url):
    html_url = requests.get(shotgun_url).text
    soup = BeautifulSoup(html_url, "lxml")
    shotguns = soup.find_all('div', class_='col-6 col-md-4 outer-tiles product-impression')
    for shotgun in shotguns:
        shotgun_name = shotgun.find('span', class_='first-line d-lg-none').text
        shotgun_price = shotgun.find('span', class_='sales').text
        shotgun_desc = shotgun.find('div', class_='pdp-link')
        shotgun_desc_url = shotgun_desc.a['href']

        print(f"-----------------------------------------------------------")
        print(f"Gun Name: {shotgun_name}")
        print(f"{shotgun_price}")
        print(f"For more info about this shotgun, Visit {shotgun_desc_url}")
        print(f"-----------------------------------------------------------")


def rifle_listings(rifle_url):
    html_url = requests.get(rifle_url).text
    soup = BeautifulSoup(html_url, "lxml")
    rifles = soup.find_all('div', class_='col-6 col-md-4 outer-tiles product-impression')
    for rifle in rifles:
        rifle_name = rifle.find('span', class_='first-line d-lg-none').text
        rifle_price = rifle.find('span', class_='sales').text
        rifle_desc = rifle.find('div', class_='pdp-link')
        rifle_desc_url = rifle_desc.a['href']

        print(f"-----------------------------------------------------------")
        print(f"{rifle_name}")
        print(f"{rifle_price}")
        print(f"For more info about this rifle, Visit {rifle_desc_url}")
        print(f"-----------------------------------------------------------")


def tatical_listings(gun_url):
    html_url = requests.get(gun_url).text
    soup = BeautifulSoup(html_url, "lxml")
    tactical_guns = soup.find_all('div', class_='col-6 col-md-4 outer-tiles product-impression')
    for tactical_gun in tactical_guns:
        tactical_gun_name = tactical_gun.find('span', class_='first-line d-lg-none').text
        tactical_gun_price = tactical_gun.find('span', class_='sales').text
        tactical_gun_desc = tactical_gun.find('div', class_='pdp-link')
        tactical_gun_desc_url = tactical_gun_desc.a['href']

        print(f"-----------------------------------------------------------")
        print(f"Gun Name: {tactical_gun_name}")
        print(f"{tactical_gun_price}")
        print(f"For more info about this tactical firearm, Visit {tactical_gun_desc_url}")
        print(f"-----------------------------------------------------------")


def search_site(handgun_url, shotgun_url, rifle_url, tactical_gun_url):
    print(f'Handgun Listings')
    print(f'-------------------------')
    handgun_listings(handgun_url)
    print('')
    print(f'Shotgun Listings')
    print(f'-------------------------')
    shotgun_listings(shotgun_url)
    print('')
    print(f'Rifle Listings')
    print(f'-------------------------')
    rifle_listings(rifle_url)
    print('')
    print(f'Tactical Gun Listings')
    print(f'-------------------------')
    tatical_listings(tactical_gun_url)
    print('')
