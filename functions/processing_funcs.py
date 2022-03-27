from functions import utils
import sys
from pydub import AudioSegment
import librosa
import soundfile as sf
    

def split_stereo_audio(voice_dir_path = './voice_data/',
                       file_regex = r'[0-9]+\.wav'):
    
    '''This function will split the stereo voice files into mono channels in the specified directories.'''
    
    mono_channel_dir = voice_dir_path + '/mono_channels/'
    
    voice_files = utils.read_dir_files(dir_path = voice_dir_path,
                                       file_regex = file_regex)
    
    total_files = len(voice_files)
    progress_cnt = 0
    
    for voice_file in voice_files:
        
        progress_cnt = progress_cnt + 1
        
        voice_file_path = voice_dir_path + voice_file
        
        voice_file_nm = utils.get_file_name(voice_file)
        
        print(f'Splitting file {progress_cnt} of {total_files} at {voice_file_path}...\n')
        
        aud_seg = AudioSegment.from_file(voice_file_path, format='wav')
        
        mono_channels = aud_seg.split_to_mono()
        
        mono_left = mono_channels[0].export(f'{mono_channel_dir}{voice_file_nm}_left.wav', format='wav')
        mono_right = mono_channels[1].export(f'{mono_channel_dir}{voice_file_nm}_right.wav', format='wav')
        
    print('Splitting complete.\n')

def remove_silence(mono_channel_dir = './voice_data/mono_channels/',
                   file_regex = r'[0-9]+\_(?:left|right)\.wav'):
    
    '''This function will sample the audio at a rate of 8kHz and attempt to remove periods of silence from mono audio channels.'''
    
    sil_rem_dir = mono_channel_dir + '/silence_removed/'
    
    voice_files = utils.read_dir_files(dir_path = mono_channel_dir,
                                       file_regex = file_regex)
    
    total_files = len(voice_files)
    
    progress_cnt = 0
    
    for voice_file in voice_files:
        
        progress_cnt = progress_cnt + 1
        
        print(f'Removing periods of silence from file {progress_cnt} of {total_files}...\n')
        
        voice_file_path = mono_channel_dir + voice_file
        
        voice_file_nm = utils.get_file_name(voice_file)
        
        # librosa.load will resample at 22.05kHz by default, but we want to use the native sampling
        # of our dataset, 8kHz, so we're specifying it here:
        audio, samp_rate = librosa.load(voice_file_path, mono = True, sr = 8000)

        # top_db is something we could play with more, tried 30 but 40 might be better:
        audio_clips = librosa.effects.split(audio, top_db=40)

        audio_data = []

        for clip in audio_clips:
            data = audio[clip[0]:clip[1]]
            audio_data.extend(data)

        sf.write(f'{sil_rem_dir}{voice_file_nm}_sil_rmvd.wav', audio_data, samp_rate)
        
    print('Removing silence process complete.\n')
    
    