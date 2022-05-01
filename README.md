# speech_recognition
UMBC DATA 606 Capstone Project

Audio data is a fascinating topic that neither of us have delved into before. While we have used machine learning for image classification and other tasks, we have not tackled any projects dealing with sound.

In particular, we want to explore what it takes to process data on voices and recognize particular speakers.

In our research, we have found several methods for doing this, but we'd like to focus on applying Deep Learning methods to see what we can accomplish with some of the latest technology.

## Goals and Objectives:

The primary goal of this project is to learn more about sound, how we perceive it as humans, and how we extract and process features from it so that a computer-based model can understand it and make decisions based off of it.

We also have the following objectives as part of our course:

Demonstrate:
    Proficiency in managing a full life-cycle data science project 
    Effective communication and presentation skills
    Competence in preparing insightful visualizations 
    Competence in writing an article
 
## Caveats:

For any packages not found on your system, you may need to install them prior to running our Python scripts. One method of doing this is:

```bash
pip3 install <package name>
```
On my RHEL 8 box, I also had to download ffmeg binary and add it to my class path. It can be downloaded from:
https://www.ffmpeg.org/download.html

## Obtaining the Data:

To build our voice recognition model, we have decided to use the following public dataset:

https://media.talkbank.org/ca/CallFriend/eng-n/0wav/

This dataset is comprised of 31 phone conversations and is ~764 MBs in size.

Given its size, we have decided not to upload it to GitHub and have written a script to download the data to a local drive:

To download the files, run the following command in the repository:

```bash
python3 get_voice_data.py
```

## Exploring the Data:

We have 31 voice files, each one a phone conversation with at least 2 speakers. In some conversations, there are periods where other speakers are present. This represents a problem for our project and for putting a system like this into production since we cannot be sure that our audio file will only contain data for 1 unique speaker.

The conversations were recorded in stereo, meaning there are 2 channels in each file. Each channel corresponds to half of the phone conversation. These channels will need to be split in processing into mono channels.

All of the audio was sampled at a rate of 8kHz. (For reference: CDs are traditionally sampled at 44.1kHz) Generally, higher sampling rate = better quality sound, but for voice data 8kHz should capture all the relevant frequencies we need and takes up less memory. For now, I think we'll stick with 8kHz.

The length of the recordings range from a little less than 8 minutes to a max of 30 minutes. We'll need to be sure we have enough data for each speaker, so some of these may need to be cut if there is not enough data.

There is background noise in the conversations that will likely need to be suppressed or removed in processing so that we focus on features of the voices as much as possible.

There will be a lot of silence that needs to be removed from the files once they are split into separate channels since when one side is talking the other is not, thus producing a period of silence in the mono channel.

## Processing the Data:

The data we are using is in stereo, so we needed to split the audio into its separate left and right channels.

We have written a script to do this that can be run with the following command:

```bash
python3 split_stereo_audio.py
```

SECTION FOR REMOVING NOISE 

Next, the periods of silence are removed from each of these files using:

```bash
python3 remove_silence.py
```

## Road Map:

Continue optimizing preprocessing functions to get clean data.

Extract most important features from the data.

Begin training a model on the data and get preliminary results.

Finalizing project:

    When various audio processing functions are ready to be combined to create a preprocessing pipeline for new audio data:

        1. Convert audio to .wav if necessary
        2. Resample using sampling rate of our dataset: 8kHz
        3. Split stereo channels to mono
        4. Remove background noise from audio
        5. Remove periods of silence from audio
        
        
## References:

Librosa blog on resampling:

https://librosa.org/blog/2019/07/17/resample-on-load/

Amazing series of YouTube videos on audio processing:

https://www.youtube.com/watch?v=iCwMQJnKk2c&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0
