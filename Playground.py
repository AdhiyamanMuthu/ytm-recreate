import streamlit as st
import process as process

st.set_page_config(
    page_title="YT-Reproduce",
    page_icon="🎞️",
    layout="wide",
)

#default credentials
valid_credentials = {
    "admin": "admin", 
}

user_name = st.sidebar.text_input('Email', type='default')
user_key = st.sidebar.text_input('Password', type='password')
login_button = st.sidebar.button("Login")

if login_button:
    if user_name in valid_credentials and user_key == valid_credentials[user_name]:
        st.sidebar.success("Login Successful!")
        st.sidebar.write('Hi ' + user_name +'!')
    else:
        st.sidebar.error("Invalid credentials. Please try again.")

page = st.sidebar.radio('Navigate', ['Studio settings', 'Produce video'])

if page == 'Produce video':
    vid_type = st.sidebar.selectbox('Select video type', ['Songs', 'Music', 'Lyrics'])
    if vid_type == 'Songs':
        st.header('Songs Recreation Factory')
        process.preview()
    if vid_type == 'Music':
        st.header('Music Recreation Factory')
        process.preview()
    if vid_type == 'Lyrics':
        st.header('Lyrics Recreation Factory')
        process.preview()




