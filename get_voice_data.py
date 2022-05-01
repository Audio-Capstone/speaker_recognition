import sys
import os
from functions import utils

if  __name__ == "__main__":
    
    print('\nThis script will download approximately 746 MB of data to the voice_data directory.\n')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('voice_data') == False:
        print('Proceed with downloading voice data?\n')
        if utils.continue_check() == False:
            sys.exit()
    voice_dir = os.path.join(os.getcwd(), 'voice_data')
    utils.get_voice_data(voice_dir)
    print('Download complete.')
    sys.exit()
            
