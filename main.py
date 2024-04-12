import streamlit as st
from time import sleep
from random import choice

st.set_page_config(
    page_title='Career Survey',
    layout='wide',
    page_icon='🎓',
)

if 'expanded' not in st.session_state:
    st.session_state.expanded = True
if 'filled_out' not in st.session_state:
    st.session_state.filled_out = False

st.title('Career Recommendation System')
st.write("Welcome to our career recommendation tool! 🌟 Please keep in mind that our algorithm is a work in progress, crafted over just four days with limited data for training. While we've done our best to provide personalized suggestions based on your survey responses, it's important to acknowledge that our results may not be as accurate as we aspire them to be. We're continuously refining our system to improve accuracy and relevance. Thank you for your understanding and patience as we evolve!")
st.divider()
st.subheader('Please answer the following questions to get started.')
with st.expander('Survey', expanded=st.session_state.expanded):
    with st.form('Survey'):
        q1 = st.toggle('I am willing to attend a 2-year or 4-year university.')
        q2 = st.toggle('I am willing to work a job with high levels of physical activity.')
        q3 = st.toggle('I am willing to work in an outdoor environment.')
        q4 = st.toggle('I am willing to work personally with clients.')
        q5 = st.toggle('I am willing to work with children.')
        if st.form_submit_button('Submit'):
            st.session_state.expanded = False
            st.session_state.filled_out = True
            st.rerun()
if st.session_state.filled_out:
    with st.spinner('Please wait while we process your responses...'):
        sleep(3)
    st.title('boobies')