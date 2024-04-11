import streamlit as st

question = 1

st.set_page_config(
    page_title='Career Survey',
    layout='wide',
    page_icon='🎓',
)

st.title('Career Recommendation System')
st.write("Welcome to our career recommendation tool! 🌟 Please keep in mind that our algorithm is a work in progress, crafted over just four days with limited data for training. While we've done our best to provide personalized suggestions based on your survey responses, it's important to acknowledge that our results may not be as accurate as we aspire them to be. We're continuously refining our system to improve accuracy and relevance. Thank you for your understanding and patience as we evolve!")
st.divider()
st.subheader('Please answer the following questions to get started.')
with st.form('Survey'):
    q1 = st.checkbox('I am currently a student or a recent graduate.')
    q2 = st.toggle('I am currently a professional.')
    q3 = st.radio('What is your current level of experience?', ['No experience', 'Less than 1 year', '1-2 years', '3-5 years', '6-10 years', '10+ years'])
    q4 = st.selectbox('What is your current level of education?', ['No education', 'High school', 'Some college', 'Bachelor\'s degree', 'Master\'s degree', 'Doctoral degree'])
    q5 = st.multiselect('What are your major(s)?', ['Computer Science', 'Computer Engineering', 'Information Systems', 'Computer Science and Engineering', 'Computer Science and Information Systems', 'Other'])
    q6 = st.select_slider('What is your current employment status?', ['Employed full-time', 'Employed part-time', 'Self-employed', 'Unemployed', 'Retired'])
    q7 = st.number_input('What is your annual salary in USD?')
    q8 = st.slider('What is your current level of stress in your life?', 0, 10)
    q9 = st.time_input('What is your current level of sleep in hours?')
    q10 = st.text_input('Where do you live?')
    if st.form_submit_button('Submit'):
        st.write('Thank you for your responses!')
        st.write('We will send you a personalized career recommendation soon.')
        answers = {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'q6': q6,
            'q7': q7,
            'q8': q8,
            'q9': q9,
            'q10': q10
        }
        print(answers)