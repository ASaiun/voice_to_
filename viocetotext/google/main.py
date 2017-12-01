#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/29/2017 9:27 AM
# @Author  : Siyuan(Saiun)
# @Site    : 
# @File    : main.py.py
# @Software: PyCharm Community Edition

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

print(client)
# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'audio.raw')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    print(audio)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')
print(config)
# Detects speech in the audio file
response = client.recognize(config, audio)
print(response)
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))