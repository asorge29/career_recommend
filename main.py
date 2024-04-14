import streamlit as st
from time import sleep
from random import choice

st.set_page_config(
    page_title='Career Survey',
    layout='wide',
    page_icon='🎓',
)

CAREER_OPTIONS = {
    'Aerospace':[1, 2, 3],
    'Engineer':[1, 3],
    'Architect':[1, 4],
    'Military':[2, 3],
    'Healthcare':[1, 2, 3, 5],
    'Computer Science':[4],
    'Environmental Science':[1, 3],
    'Cullinary':[2, 4, 5],
    'Agriculture':[2, 3],
    'Teaching':[1, 4, 5],
    'Construction':[2, 3, 4],
    'Finance':[1, 4],
    'Marketing':[1, 4]
}

INTERESTS = {
    'Art': 101,
    'Technology': 102,
    'Science': 103,
    'Music': 104,
    'Sports': 105,
    'Writing': 106,
    'Cooking': 107,
    'Fashion': 108,
    'Health & Fitness': 109,
    'Photography': 110,
    'Travel': 111,
    'Nature & Environment': 112,
    'History': 113,
    'Film & Television': 114,
    'Gaming': 115,
    'Graphic Design': 116,
    'Coding': 117,
    'Psychology': 118,
    'Dance': 119,
    'Automobiles': 120,
    'Entrepreneurship': 121,
    'Animals & Pets': 122,
    'Reading': 123,
    'Social Media': 124,
    'Astronomy': 125,
    'Politics': 126,
    'Sculpture': 127,
    'Interior Design': 128,
    'Martial Arts': 129,
    'Baking': 130,
    'Graphic Novels & Comics': 131,
    'Architecture': 132,
    'Yoga & Meditation': 133,
    'Aviation': 134,
    'Cycling': 135,
    'DIY & Crafts': 136,
    'Theater': 137,
    'Urban Planning': 138,
    'Animation': 139,
    'Law & Justice': 140,
    'Foreign Languages': 141,
    'Fishing': 142,
    'Board Games': 143,
    'Education': 144,
    'Philosophy': 145,
    'Magic & Illusion': 146,
    'Camping & Hiking': 147,
    'Social Work': 148,
    'Surfing': 149,
    'DIY Electronics': 150
}

def eliminate_options(responses: list, options: dict):
    eliminated_options = []
    passed_options = []
    for i in range(len(responses)):
        for j in range(len(options)):
            if responses[i] in list(options.values())[j] and list(options.keys())[j] not in eliminated_options:
                removed = list(options.keys())[j]
                eliminated_options.append(removed)
    for key in options.keys():
        if key not in eliminated_options:
            passed_options.append(key)
    return passed_options, eliminated_options

def sort_by_interest(met_criteria:list, not_met:list, interests):
    pass

st.title('Career Recommendation System')
st.write("Welcome to our career recommendation tool! 🌟 Please keep in mind that our algorithm is a work in progress, crafted over just four days with limited data for training. While we've done our best to provide personalized suggestions based on your survey responses, it's important to acknowledge that our results may not be as accurate as we aspire them to be. We're continuously refining our system to improve accuracy and relevance. Thank you for your understanding and patience as we evolve!")
st.divider()
st.subheader('Please answer the following questions to get started.')
with st.expander('Survey'):
    with st.form('Survey'):
        q1 = st.toggle('I am willing to attend a 2-year or 4-year university.')
        q2 = st.toggle('I am willing to work a job with high levels of physical activity.')
        q3 = st.toggle('I am willing to work in an outdoor environment.')
        q4 = st.toggle('I am willing to work personally with clients.')
        q5 = st.toggle('I am willing to work with children.')
        responses = [q1, q2, q3, q4, q5]
        interests = st.multiselect('Select all that interest you:', list(INTERESTS.keys()))
        if st.form_submit_button('Submit'):
            response_numbers = []
            for i in range(len(responses)):
                if not responses[i]:
                    response_numbers.append(i + 1)