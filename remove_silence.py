import sys
from functions import processing_funcs, utils
        
if  __name__ == "__main__":
    
    print('\nThis script will remove periods of silence from audio files in voice_data/mono_channels/.')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('./voice_data/mono_channels/silence_removed/') == False:
        print('Proceed with removing silence from voice data?')
        if utils.continue_check() == False:
            sys.exit()
    processing_funcs.remove_silence()
    sys.exit()