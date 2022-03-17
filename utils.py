import os
import errno

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