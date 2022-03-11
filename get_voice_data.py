import os
import errno
import requests
from bs4 import BeautifulSoup

def confirm_download():
    
    cont_cmd = input('This function will download approximately 746 MB of data to the voice_data directory. Continue? (Y/N)\n')
    
    if cont_cmd.upper() == 'Y':
        print('Continuing download...\n')
        make_vd_dir()
    elif cont_cmd.upper() == 'N':
        print('Aborting file download.\n')
        return
    else:
        print("Input not valid, aborting file download.\n")
        return

def make_vd_dir():
    '''This function creates a local directory, voice_data, to store all the voice data files.'''
    
    try:
        print('Creating voice_data directory...\n')
        os.makedirs('voice_data')
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise
        print('voice_data directory already exists.\n')

        cont_cmd = input('Continue with downloading voice data? (Y/N)\n')

        if cont_cmd.upper() == 'Y':
            print('Continuing file download...\n')
            get_voice_data()
        elif cont_cmd.upper() == 'N':
            print('Aborting file download.\n')
            return
        else:
            print("Input not valid, aborting file download.\n")
            return

def get_voice_data():
    '''This function will download the voice data into a local folder.'''

    url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/'

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    
    vd_dir = 'voice_data/'

    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    for url in urls[5:]:
        vd_file = vd_dir + url
        with open(vd_file, 'wb') as f_out:
            url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/' + url
            f_out.write(requests.get(url).content)
            print('Download complete.')

if  __name__ == "__main__":
    confirm_download()