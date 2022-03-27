# import utils
# import sys
# import os
# from pydub import AudioSegment
# import regex as re

import sys
from functions import processing_funcs, utils

if  __name__ == "__main__":
    
    print('\nThis script will split stereo channels in voice_data directory into mono channels.')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('./voice_data/mono_channels') == False:
        print('Proceed with splitting voice data?')
        if utils.continue_check() == False:
            sys.exit()
    processing_funcs.split_stereo_audio()
    sys.exit()
    