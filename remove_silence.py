import utils
import sys
import os
import librosa
import re
import soundfile as sf

def remove_silence():
    mono_audio_dir = './voice_data/mono_channels/'
    sil_rem_dir = mono_audio_dir + '/silence_removed/'
    voice_files = [file for file in os.listdir(mono_audio_dir) if re.match(r'[0-9]+\_(?:left|right)\.wav', file)]
    
    total_files = len(voice_files)
    start_file = 0
    
    for voice_file in voice_files:
        start_file = start_file + 1
        
        print(f'Removing periods of silence from file {start_file} of {total_files}...\n')
        
        file_name = voice_file[:-4]
        
        voice_file_fp = mono_audio_dir + voice_file
        voice_file_nm = voice_file[:-4]
        
        audio, samp_rate = librosa.load(voice_file_fp, mono=True)

        audio_clips = librosa.effects.split(audio, top_db=30)

        audio_data = []

        for clip in audio_clips:
            data = audio[clip[0]:clip[1]]
            audio_data.extend(data)

        sf.write(f'{sil_rem_dir}{voice_file_nm}_sil_rmvd.wav', audio_data, samp_rate)
        
    print('Removing silence process complete.\n')
        
        
if  __name__ == "__main__":
    
    print('\nThis script will remove periods of silence from audio files in voice_data/mono_channels/.')
    if utils.continue_check() == False:
        sys.exit()
    if utils.make_dir('./voice_data/mono_channels/silence_removed/') == False:
        print('Proceed with removing silence from voice data?')
        if utils.continue_check() == False:
            sys.exit()
    remove_silence()
    sys.exit()