import os
import re
from pytube import YouTube
import streamlit as st

AUDIO_PATH  = os.getcwd() + '\\raw-music' 

def get_audio(url):
    pattern = r'v=([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    
    if match:
        group_id = match.group(1)
        print(group_id)
    else:
        st.error("Could not generate group id")

    yt = YouTube(url)
    mp3_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    mp3_stream.download(output_path = AUDIO_PATH, filename=group_id + '.mp3')
    return AUDIO_PATH + '\\' + group_id + '.mp3'

def preview():
    url = st.text_input('YT Url')
    image_path = st.text_input('Image path')
    generate = st.button('Preview')
    if generate:
        audio = get_audio(url)
        st.audio(audio)
        st.image(image_path)
        upload = st.button('Upload')