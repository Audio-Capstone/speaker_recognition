import sys
import os
from functions import processing_funcs, utils
        
if  __name__ == "__main__":
    
    print('\nThis script will remove periods of silence from audio files in voice_data/mono_channels/.')
    if utils.continue_check() == False:
        sys.exit()
    new_dir = os.path.join(os.getcwd(), 'voice_data', 'mono_channels', 'silence_removed')
    if utils.make_dir(new_dir) == False:
        print('Proceed with removing silence from voice data?')
        if utils.continue_check() == False:
            sys.exit()
    processing_funcs.remove_silence()
    sys.exit()
