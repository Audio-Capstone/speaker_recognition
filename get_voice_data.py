import requests
from bs4 import BeautifulSoup

def get_voice_data():
    '''This function will download the voice data into a local folder.'''

    url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/'

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []

    for link in soup.find_all('a'):
        urls.append(link.get('href'))
        print(link.get('href'))

    for url in urls[5:]:
        with open(url, 'wb') as f_out:
            url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/' + url
            f_out.write(requests.get(url).content)


if  __name__ == "__main__":
    print('Collecting voice data...')
    get_voice_data()

