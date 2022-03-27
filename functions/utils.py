import os
import errno
import regex as re

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
    
def read_dir_files(dir_path = '.voice_data/',
                   file_regex = r'[0-9]+\.wav'):
    
    print(f'Collecting all files in {dir_path} matching regular expression {file_regex}.\n')
    
    # Based on https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
    file_list = [file for file in os.listdir(dir_path) if re.match(file_regex, file)]
    
    return file_list
    