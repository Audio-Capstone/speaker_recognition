import requests
import sys
from bs4 import BeautifulSoup
import utils

def get_voice_data():
    '''This function will download the voice data into a local folder.'''

    url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/'

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    
    vd_dir = 'voice_data/'

    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    total_files = len(urls[5:])
    start_file = 0
    
    for url in urls[5:]:
        start_file = start_file + 1
        print(f'Downloading file {start_file} of {total_files}...\n')
        vd_file = vd_dir + url
        with open(vd_file, 'wb') as f_out:
            url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/' + url
            f_out.write(requests.get(url).content)

if  __name__ == "__main__":
    
    print('\nThis script will download approximately 746 MB of data to the voice_data directory.\n')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('voice_data') == False:
        print('Proceed with downloading voice data?\n')
        if utils.continue_check() == False:
            sys.exit()
    get_voice_data()
    print('Download complete.')
    sys.exit()
            