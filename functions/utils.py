import requests
from bs4 import BeautifulSoup
import os
import errno
import regex as re
from pydub.utils import mediainfo

def get_file_name(voice_file):
    
    # Return name of file before '.':
    return voice_file.split('.')[0]

def continue_check():
    
    cont_cmd = input('Continue? (Y \ N)\n')
    
    if cont_cmd.upper() == 'Y':
        print('Continuing...\n')
        return True
    elif cont_cmd.upper() == 'N':
        print('Aborting.\n')
        return False
    else:
        print("Input not valid, aborting.\n")
        return False
    
def make_dir(new_dir_path):

    try:
        print(f'Creating directory at {new_dir_path}...\n')
        os.makedirs(new_dir_path)
        return True
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise
        print(f'{new_dir_path} already exists.\n')
        return False
    
def get_file_duration(file_path, minutes=False):
    file_duration_secs = mediainfo(file_path)['duration']
    if minutes == True:
        file_duration_mins = round((float(file_duration_secs) / 60), 2)
        return file_duration_mins
    return file_duration_secs
    
def read_dir_files(dir_path = 'voice_data',
                   file_regex = r'[0-9]+\.wav'):
    
    print(f'Collecting all files in {dir_path} matching regular expression {file_regex}.\n')
    
    # Based on https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
    if file_regex == None:
        file_list = os.listdir(dir_path)
    else:
        file_list = [file for file in os.listdir(dir_path) if re.match(file_regex, file)]
    
    return file_list

def del_dir_files(dir_path=None, check=True, verbose=False):
    '''Deletes all files in specified directory. Use with caution!'''
    num_files = len(read_dir_files(dir_path, file_regex=None))
    print(f'Directory at path {dir_path} contains {num_files} files.')
    
    if check == True:
        print(f'Continue with deleting all files in {dir_path}?')
        if continue_check() == True:
            pass
        else:
            return
        
    for file in os.scandir(dir_path):
        if verbose == True:
            print(f'Removing {file}.')
        os.remove(file.path)
    
    print(f'Removal of all files in {dir_path} complete.')
    
def get_voice_data(voice_dir):
    '''This function will download the voice data into a local folder.'''

    url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/'

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []

    vd_dir = voice_dir

    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    total_files = len(urls[5:])
    progress_cnt = 0
    progress_prcnt = 0
    prcnt_print = 0

    print(f'Downloading {total_files} files from {url}')

    for url in urls[5:]:
        progress_cnt = progress_cnt + 1
        vd_file = os.path.join(vd_dir, url)
        with open(vd_file, 'wb') as f_out:
            url = 'https://media.talkbank.org/ca/CallFriend/eng-n/0wav/' + url
            f_out.write(requests.get(url).content)

        progress_prcnt = progress_cnt / total_files
        if progress_prcnt >= prcnt_print + 0.1:
            print("{}% done...".format(round(progress_prcnt * 100, 2)))
            prcnt_print += 0.1
    print(f'All {total_files} downloaded to the {vd_dir} directory')

def clear_train_test_dirs():
    training_dirs = os.listdir(train_top_dir)
    testing_dirs = os.listdir(test_top_dir)
                
    for train_dir in training_dirs:
        utils.del_dir_files(dir_path=os.path.join(train_top_dir, train_dir), check=False, verbose=False)
                                        
    for testing_dir in testing_dirs:
        utils.del_dir_files(dir_path=os.path.join(test_top_dir, testing_dir), check=False, verbose=False)
