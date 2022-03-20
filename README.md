# speech_recognition
UMBC DATA 606 Capstone Project

## Caveats

For any packages not found on your system, you may need to install them prior to running our Python scripts. One method of doing this is:

```bash
pip3 install <package name>
```
On my RHEL 8 box, I also had to download ffmeg binary and add it to my class path. It can be downloaded from:
https://www.ffmpeg.org/download.html

## Obtain data

To get started, you need to obtain some audio files. We obtained the files for our project from:
https://media.talkbank.org/ca/CallFriend/eng-n/0wav/ 

```bash
python3 get_voice_data.py
```

## Process data

The data we are using is in stereo, so we needed to split the audio into its separate left and right channels. 

```bash
python3 split_stereo_audio.py
```
Next, the periods of silence are removed from each of these files using:

```bash
python3 remove_silence.py
```

