from bs4 import BeautifulSoup
import requests

def check_updates(app_website, current_version):
    html_url = requests.get(app_website).text
    soup = BeautifulSoup(html_url, "lxml")
    update_check = soup.find('td', class_='Current_Version').text

    if current_version == update_check:
        print(f'There are currently no updates available')
    elif current_version >= update_check:
        print(f'Error: Please contact developers....')
        print(f'Current Version {current_version}')
        print(f'Update Check: {update_check}')
        print(f'The current program version {current_version} does not exist yet...'
              f'Check our website for the most current version {update_check}')
        exit(0)
    else:
        print(f'There is a update available')

