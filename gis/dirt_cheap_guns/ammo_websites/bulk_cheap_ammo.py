from bs4 import BeautifulSoup
import requests

def find_12_gauge(twelve_gauge_url):
    html_url = requests.get(twelve_gauge_url).text
    soup = BeautifulSoup(html_url, "lxml")
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_16_gauge(sixteen_gauge_url):
    html_url = requests.get(sixteen_gauge_url).text
    soup = BeautifulSoup(html_url, "lxml")
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_20_gauge(twenty_gauge_url):
    html_url = requests.get(twenty_gauge_url).text
    soup = BeautifulSoup(html_url, "lxml")
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    gunprimes = soup.find_all('div', class_='product-list-data-box-main gunprime.com')

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for gunprime in gunprimes:
        ammo_name = gunprime.find('span', class_='description').text
        ammo_grain = gunprime.find('div', class_='grains').text
        ammo_price = gunprime.find('div', class_='price').text
        ammo_desc_url = gunprime.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_410(fourten_url):
    html_url = requests.get(fourten_url).text
    soup = BeautifulSoup(html_url, "lxml")
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    gunprimes = soup.find_all('div', class_='product-list-data-box-main gunprime.com')

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for gunprime in gunprimes:
        ammo_name = gunprime.find('span', class_='description').text
        ammo_grain = gunprime.find('div', class_='grains').text
        ammo_price = gunprime.find('div', class_='price').text
        ammo_desc_url = gunprime.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        # print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_22_lr(twenty_two_lr_url):
    html_url = requests.get(twenty_two_lr_url).text
    soup = BeautifulSoup(html_url, "lxml")
    zincpoints = soup.find_all('div', class_='product-list-data-box retailer-link zincpoint.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    twoammos = soup.find_all('div', class_='product-list-data-box-main 2ammunition.com')
    natchezss_ammos = soup.find_all('div', class_='product-list-data-box-main natchezss.com')
    twoawareammos = soup.find_all('div', class_='product-list-data-box-main 2awarehouse.com')


    for zincpoint in zincpoints:
        ammo_name = zincpoint.find('span', class_='description').text
        ammo_grain = zincpoint.find('div', class_='grains').text
        ammo_price = zincpoint.find('div', class_='price').text
        ammo_desc_url = zincpoint.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoammo in twoammos:
        ammo_name = twoammo.find('span', class_='description').text
        ammo_grain = twoammo.find('div', class_='grains').text
        ammo_price = twoammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for natchezss_ammo in natchezss_ammos:
        ammo_name = natchezss_ammo.find('span', class_='description').text
        ammo_grain = natchezss_ammo.find('div', class_='grains').text
        ammo_price = natchezss_ammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoawareammo in twoawareammos:
        ammo_name = twoawareammo.find('span', class_='description').text
        ammo_grain = twoawareammo.find('div', class_='grains').text
        ammo_price = twoawareammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_9mm(nine_mm_url):
    html_url = requests.get(nine_mm_url).text
    soup = BeautifulSoup(html_url, "lxml")
    zincpoints = soup.find_all('div', class_='product-list-data-box retailer-link zincpoint.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    twoammos = soup.find_all('div', class_='product-list-data-box-main 2ammunition.com')
    natchezss_ammos = soup.find_all('div', class_='product-list-data-box-main natchezss.com')
    twoawareammos = soup.find_all('div', class_='product-list-data-box-main 2awarehouse.com')


    for zincpoint in zincpoints:
        ammo_name = zincpoint.find('span', class_='description').text
        ammo_grain = zincpoint.find('div', class_='grains').text
        ammo_price = zincpoint.find('div', class_='price').text
        ammo_desc_url = zincpoint.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoammo in twoammos:
        ammo_name = twoammo.find('span', class_='description').text
        ammo_grain = twoammo.find('div', class_='grains').text
        ammo_price = twoammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for natchezss_ammo in natchezss_ammos:
        ammo_name = natchezss_ammo.find('span', class_='description').text
        ammo_grain = natchezss_ammo.find('div', class_='grains').text
        ammo_price = natchezss_ammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoawareammo in twoawareammos:
        ammo_name = twoawareammo.find('span', class_='description').text
        ammo_grain = twoawareammo.find('div', class_='grains').text
        ammo_price = twoawareammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

def find_556_nato(fivefivesix_nato_url):
    html_url = requests.get(fivefivesix_nato_url).text
    soup = BeautifulSoup(html_url, "lxml")
    zincpoints = soup.find_all('div', class_='product-list-data-box retailer-link zincpoint.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    twoammos = soup.find_all('div', class_='product-list-data-box-main 2ammunition.com')
    natchezss_ammos = soup.find_all('div', class_='product-list-data-box-main natchezss.com')
    twoawareammos = soup.find_all('div', class_='product-list-data-box-main 2awarehouse.com')


    for zincpoint in zincpoints:
        ammo_name = zincpoint.find('span', class_='description').text
        ammo_grain = zincpoint.find('div', class_='grains').text
        ammo_price = zincpoint.find('div', class_='price').text
        ammo_desc_url = zincpoint.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoammo in twoammos:
        ammo_name = twoammo.find('span', class_='description').text
        ammo_grain = twoammo.find('div', class_='grains').text
        ammo_price = twoammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for natchezss_ammo in natchezss_ammos:
        ammo_name = natchezss_ammo.find('span', class_='description').text
        ammo_grain = natchezss_ammo.find('div', class_='grains').text
        ammo_price = natchezss_ammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoawareammo in twoawareammos:
        ammo_name = twoawareammo.find('span', class_='description').text
        ammo_grain = twoawareammo.find('div', class_='grains').text
        ammo_price = twoawareammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")


def find_762_mm(sevensixtwo_mm_url):
    html_url = requests.get(sevensixtwo_mm_url).text
    soup = BeautifulSoup(html_url, "lxml")
    zincpoints = soup.find_all('div', class_='product-list-data-box retailer-link zincpoint.com')
    sharkcoastals = soup.find_all('div', class_='product-list-data-box-main sharkcoasttactical.com')
    ammodepots = soup.find_all('div', class_='product-list-data-box-main ammunitiondepot.com')
    justincaseammos = soup.find_all('div', class_='product-list-data-box-main justincaseammo.com')
    trueshotgunclubs = soup.find_all('div', class_='product-list-data-box-main trueshotgunclub.com')
    twoammos = soup.find_all('div', class_='product-list-data-box-main 2ammunition.com')
    natchezss_ammos = soup.find_all('div', class_='product-list-data-box-main natchezss.com')
    twoawareammos = soup.find_all('div', class_='product-list-data-box-main 2awarehouse.com')


    for zincpoint in zincpoints:
        ammo_name = zincpoint.find('span', class_='description').text
        ammo_grain = zincpoint.find('div', class_='grains').text
        ammo_price = zincpoint.find('div', class_='price').text
        ammo_desc_url = zincpoint.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for sharkcoastal in sharkcoastals:
        ammo_name = sharkcoastal.find('span', class_='description').text
        ammo_grain = sharkcoastal.find('div', class_='grains').text
        ammo_price = sharkcoastal.find('div', class_='price').text
        ammo_desc_url = sharkcoastal.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for ammodepot in ammodepots:
        ammo_name = ammodepot.find('span', class_='description').text
        ammo_grain = ammodepot.find('div', class_='grains').text
        ammo_price = ammodepot.find('div', class_='price').text
        ammo_desc_url = ammodepot.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for justincaseammo in justincaseammos:
        ammo_name = justincaseammo.find('span', class_='description').text
        ammo_grain = justincaseammo.find('div', class_='grains').text
        ammo_price = justincaseammo.find('div', class_='price').text
        ammo_desc_url = justincaseammo.find('', class_='')

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for trueshotgunclub in trueshotgunclubs:
        ammo_name = trueshotgunclub.find('span', class_='description').text
        ammo_grain = trueshotgunclub.find('div', class_='grains').text
        ammo_price = trueshotgunclub.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoammo in twoammos:
        ammo_name = twoammo.find('span', class_='description').text
        ammo_grain = twoammo.find('div', class_='grains').text
        ammo_price = twoammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for natchezss_ammo in natchezss_ammos:
        ammo_name = natchezss_ammo.find('span', class_='description').text
        ammo_grain = natchezss_ammo.find('div', class_='grains').text
        ammo_price = natchezss_ammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")

    for twoawareammo in twoawareammos:
        ammo_name = twoawareammo.find('span', class_='description').text
        ammo_grain = twoawareammo.find('div', class_='grains').text
        ammo_price = twoawareammo.find('div', class_='price').text

        print(f"-----------------------------------------------------------")
        print(f"Ammo Name: {ammo_name}")
        print(f"Ammo Grain: {ammo_grain}")
        print(f"{ammo_price}")
        #print(f"For more info about this handgun, Visit {ammo_desc_url}")
        print(f"-----------------------------------------------------------")


def search_site(twelve_gauge_url, sixteen_gauge_url, twenty_gauge_url, fourten_url,nine_mm_url, fivefivesix_nato_url, sevensixtwo_mm_url):
    print(f'12 guage Ammo Listings')
    print(f'-------------------------')
    find_12_gauge(twelve_gauge_url)
    print('')
    print(f'16 gauge Ammo Listings')
    print(f'-------------------------')
    find_16_gauge(sixteen_gauge_url)
    print('')
    print(f'20 gauge Ammo Listings')
    print(f'-------------------------')
    find_20_gauge(twenty_gauge_url)
    print('')
    print(f'410 Bore Ammo Listings')
    print(f'-------------------------')
    find_410(fourten_url)
    print('')
    print(f'9mm Ammo Listings')
    print(f'-------------------------')
    find_9mm(nine_mm_url)
    print('')
    print(f'5.56x45mm Ammo Listings')
    print(f'-------------------------')
    find_556_nato(fivefivesix_nato_url)
    print('')
    print(f'7.62x39mm Ammo Listings')
    print(f'-------------------------')