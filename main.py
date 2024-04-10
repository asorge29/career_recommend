import streamlit as st

question = 1

st.set_page_config(
    page_title='Career Survey',
    layout='wide',
    page_icon='🎓',
)

st.title('Career Recommendation System')
st.header('Take the survey and we will recommend you the best career!')
with st.form('User Input'):
    if st.form_submit_button('Submit'):
        pass

if question == 1:
        if st.button("place holder"):
            pass

st.header('Recommending place holder')