import utils
import sys
import os
from pydub import AudioSegment
import regex as re

def split_stereo_audio(voice_data_dir='./voice_data/',
                       mono_channel_dir='./voice_data/mono_channels/'):
    # Based on https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
    voice_files = [file for file in os.listdir('./voice_data/') if re.match(r'[0-9]+\.wav', file)]
    
    total_files = len(voice_files)
    start_file = 0
    
    for voice_file in voice_files:
        start_file = start_file + 1
        
        voice_file_fp = voice_data_dir + voice_file
        voice_file_nm = voice_file[0:4]
        
        print(f'Splitting file {start_file} of {total_files} at {voice_file_fp}...\n')
        
        aud_seg = AudioSegment.from_file(voice_file_fp, format='wav')
        mono_channels = aud_seg.split_to_mono()
        
        mono_left = mono_channels[0].export(f'{mono_channel_dir}{voice_file_nm}_left.wav', format='wav')
        mono_right = mono_channels[1].export(f'{mono_channel_dir}{voice_file_nm}_right.wav', format='wav')
        
    print('Splitting complete.\n')

if  __name__ == "__main__":
    
    print('\nThis script will split stereo channels in voice_data directory into mono channels.')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('./voice_data/mono_channels') == False:
        print('Proceed with splitting voice data?')
        if utils.continue_check() == False:
            sys.exit()
    split_stereo_audio()
    sys.exit()
    