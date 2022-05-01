from functions import utils
import sys
from pydub import AudioSegment
import librosa
import soundfile as sf
import noisereduce as nr
import os    

def split_stereo_audio(voice_dir_path = 'voice_data',
                       sub_dir_path = 'mono_channels',
                       file_regex = r'[0-9]+\.wav'):
    
    '''This function will split the stereo voice files into mono channels in the specified directories.'''
    
    mono_channel_dir = os.path.join(voice_dir_path, sub_dir_path)

    voice_files = utils.read_dir_files(dir_path = voice_dir_path,
                                       file_regex = file_regex)

    total_files = len(voice_files)
    progress_cnt = 0
    
    for voice_file in voice_files:
        
        progress_cnt = progress_cnt + 1
        
        voice_file_path = os.path.join(voice_dir_path, voice_file)
        
        voice_file_nm = utils.get_file_name(voice_file)
        
        print(f'Splitting file {progress_cnt} of {total_files} at {voice_file_path}...\n')
        
        aud_seg = AudioSegment.from_file(voice_file_path, format='wav')
       
        mono_channels = aud_seg.split_to_mono()

        mono_L_nm = os.path.join(mono_channel_dir, voice_file_nm + "_L.wav")
        mono_R_nm = os.path.join(mono_channel_dir, voice_file_nm + "_R.wav")

        mono_left = mono_channels[0].export(mono_L_nm, format='wav')
        mono_right = mono_channels[1].export(mono_R_nm, format='wav')
        
    print('Splitting complete.\n')
    
    
    
def reduce_noise(voice_dir_path = 'voice_data',
                 sub_dir_path = 'mono_channels',
                 samp_rate = 8000,
                 file_regex = r'[0-9]+\_(?:L|R)\.wav'):
    
    '''This function will remove noise from the audio files.'''
    
    mono_channel_dir = os.path.join(voice_dir_path, sub_dir_path)
    
    voice_files = utils.read_dir_files(dir_path = mono_channel_dir,
                                       file_regex = file_regex)
    
    total_files = len(voice_files)
    progress_cnt = 0
    
    for voice_file in voice_files:
        
        progress_cnt = progress_cnt + 1
        
        voice_file_path = os.path.join(mono_channel_dir, voice_file)
        
        voice_file_nm = utils.get_file_name(voice_file)
        
        print(f'Removing noise from file {progress_cnt} of {total_files} at {voice_file_path}...\n')
        
        audio = librosa.load(voice_file_path, mono = True, sr = samp_rate)[0] # Indexed at 0 since we only need the audio return
        
        audio_rdcd_nse = nr.reduce_noise(y=audio, sr=samp_rate)
        
        sf.write(voice_file_path, audio_rdcd_nse, samp_rate)
        
    print('Noise reduction complete.\n')   
    
    

def remove_silence(mono_channel_dir = 'voice_data/mono_channels',
                   sil_rem_dir_path = 'silence_removed',
                   file_regex = r'[0-9]+\_(?:L|R)\.wav'): 
    
    '''This function will sample the audio at a rate of 8kHz and attempt to remove periods of silence from mono audio channels.'''
    
    sil_rem_dir = os.path.join(mono_channel_dir, sil_rem_dir_path)
    
    voice_files = utils.read_dir_files(dir_path = mono_channel_dir,
                                       file_regex = file_regex)
    
    total_files = len(voice_files)
    
    progress_cnt = 0
    
    for voice_file in voice_files:
        
        progress_cnt = progress_cnt + 1
        
        print(f'Removing periods of silence from file {progress_cnt} of {total_files}...\n')
        
        voice_file_path = os.path.join(mono_channel_dir, voice_file)
        
        voice_file_nm = utils.get_file_name(voice_file)
        
        # librosa.load will resample at 22.05kHz by default, but we want to use the native sampling
        # of our dataset, 8kHz, so we're specifying it here:
        audio, samp_rate = librosa.load(voice_file_path, mono = True, sr = 8000)

        # top_db is something we could play with more, using 30 based on limited testing:
        audio_clips = librosa.effects.split(audio, top_db=30)

        audio_data = []

        for clip in audio_clips:
            data = audio[clip[0]:clip[1]]
            audio_data.extend(data)
        
        file_to_write = os.path.join(sil_rem_dir, voice_file_nm + "_sil_rmvd.wav")
        sf.write(file_to_write, audio_data, samp_rate)
        
    print('Removing silence process complete.\n')
    

   
    
    
