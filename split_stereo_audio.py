import os
import sys
from functions import processing_funcs, utils

if  __name__ == "__main__":
    
    print('\nThis script will split stereo channels in voice_data directory into mono channels.')
    if utils.continue_check() == False:
        sys.exit()
    new_dir = os.path.join(os.getcwd(), 'voice_data', 'mono_channels')
    if utils.make_dir(new_dir) == False:
        print('Proceed with splitting voice data?')
        if utils.continue_check() == False:
            sys.exit()
    processing_funcs.split_stereo_audio()
    sys.exit()
    
