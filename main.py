import streamlit as st
from time import sleep
from random import choice

st.set_page_config(
    page_title='Career Survey',
    layout='wide',
    page_icon='🎓',
)

CAREER_OPTIONS = {
    'Aerospace': [1, 2, 3, 112, 134, 125, 106, 110, 145, 107],
    'Engineer': [1, 3, 102, 113, 133, 127, 148, 131, 109],
    'Architect': [1, 4, 102, 127, 132, 110, 111, 116],
    'Military': [2, 3, 105, 134, 112, 106, 139, 145],
    'Healthcare': [1, 2, 3, 5, 109, 118, 119, 148, 126, 142],
    'Computer Science': [4, 102, 117, 106, 103, 101],
    'Environmental Science': [1, 3, 112, 125, 111, 147, 141, 118],
    'Culinary': [2, 4, 5, 107, 130, 110, 123, 109, 141, 136],
    'Agriculture': [2, 3, 112, 141, 146, 148, 130, 110, 142],
    'Teaching': [1, 4, 5, 144, 123, 113, 148, 136, 141, 107],
    'Construction': [2, 3, 4, 107, 132, 130, 110, 103, 141, 139],
    'Finance': [1, 4, 102, 140, 145, 111, 119, 123],
    'Marketing': [1, 4, 114, 123, 124, 111, 109, 114],
    'Software Developer': [4, 102, 117, 106, 103, 101],
    'Graphic Designer': [4, 101, 116, 107],
    'Data Scientist': [1, 102, 106, 103, 109],
    'Civil Engineer': [1, 2, 102, 107, 127, 132, 141, 139],
    'Marketing Manager': [1, 4, 114, 123, 124, 111, 109, 114],
    'Teacher': [1, 4, 5, 144, 123, 113, 148, 136, 141, 107],
    'Nurse': [1, 2, 3, 5, 109, 118, 119, 148, 126, 142],
    'Chef': [2, 4, 5, 107, 130, 110, 123, 109, 141, 136],
    'Mechanical Engineer': [1, 2, 102, 107, 127, 141, 139],
    'Electrician': [2, 3, 4, 107, 130, 110, 141, 139],
    'Photographer': [4, 101, 110, 114],
    'Architect': [1, 4, 102, 127, 132, 110, 111, 116],
    'Financial Analyst': [1, 4, 102, 140, 145, 111, 119, 123],
    'Lawyer': [1, 4, 113, 140, 145, 109, 126],
    'Dentist': [1, 109, 118, 119, 126, 142],
    'Police Officer': [1, 2, 3, 105, 106, 139, 145],
    'Firefighter': [2, 3, 105, 106, 139, 145],
    'Pilot': [1, 3, 102, 134, 141],
    'Biologist': [1, 3, 102, 103, 112, 118, 125],
    'Event Planner': [4, 101, 114, 123, 109],
    'Social Worker': [1, 4, 101, 123, 109, 148],
    'Pharmacist': [1, 109, 118, 119, 126],
    'Interior Designer': [4, 101, 110, 107, 123, 128],
    'Electrician': [2, 3, 4, 107, 130, 110, 141, 139],
    'Psychologist': [1, 4, 101, 118, 119, 126, 148],
    'Actor': [4, 106, 107, 114, 137],
    'Fitness Trainer': [2, 4, 5, 109, 118, 119, 126],
    'Real Estate Agent': [4, 107, 123, 126],
    'Mechanic': [2, 4, 107, 130, 110, 139],
    'Fashion Designer': [4, 101, 107, 110, 123, 108],
    'Biomedical Engineer': [1, 102, 107, 127, 141],
    'Geologist': [1, 3, 102, 103, 112, 118, 125],
    'Journalist': [4, 101, 106, 109, 114],
    'Human Resources Manager': [1, 4, 114, 123, 109],
    'Plumber': [2, 3, 4, 107, 130, 110, 141, 139],
    'Accountant': [1, 4, 102, 140, 145, 111, 119],
    'Dietitian': [1, 109, 118, 119, 126, 142],
    'Biotechnologist': [1, 102, 107, 112, 141],
    'Electrician': [2, 3, 4, 107, 130, 110, 141, 139],
    'Paramedic': [2, 3, 5, 109, 118, 119, 126],
    'Painter': [2, 3, 4, 107, 130, 110, 141],
    'Computer Programmer': [4, 102, 117, 106, 103, 101],
    'Veterinarian': [1, 109, 118, 119, 126, 142],
    'Mechanical Engineer': [1, 2, 102, 107, 127, 141, 139],
    'Chemical Engineer': [1, 2, 102, 107, 127, 141, 139],
    'Aerospace Engineer': [1, 2, 3, 112, 134, 125, 106, 110, 145, 107],
    'Physicist': [1, 102, 103, 125, 118],
    'Mathematician': [1, 102, 103, 125, 118],
    'Translator': [4, 101, 141, 123],
    'Speech Therapist': [1, 109, 118, 119, 126],
    'Bartender': [2, 4, 107, 123, 109],
    'Agricultural Engineer': [1, 2, 102, 107, 112, 141],
    'Forester': [2, 3, 112, 141, 147],
    'Marine Biologist': [1, 3, 112, 118, 125],
    'Zoologist': [1, 3, 112, 118, 125],
    'Social Media Manager': [1, 4, 114, 123, 124, 111, 109],
    'Web Designer': [4, 102, 106, 110, 101],
    'Fashion Stylist': [4, 101, 107, 110, 123, 108],
    'Event Coordinator': [4, 101, 114, 123, 109],
    'Investment Banker': [1, 4, 102, 140, 145, 111, 119],
    'Surveyor': [1, 2, 3, 107, 132, 141, 147],
    'Electrician': [2, 3, 4, 107, 130, 110, 141, 139],
    'Carpenter': [2, 3, 4, 107, 130, 110, 141, 139],
    'Librarian': [1, 4, 101, 123, 109],
    'Air Traffic Controller': [1, 102, 106, 134, 141],
    'Hotel Manager': [1, 4, 114, 123, 109],
    'Chiropractor': [1, 109, 118, 119, 126],
    'Security Guard': [2, 106, 139, 145],
    'Insurance Agent': [1, 4, 102, 140, 145, 111, 119],
    'Environmental Engineer': [1, 2, 3, 112, 125, 110, 141],
    'Economist': [1, 4, 102, 140, 145, 111, 119],
    'Dancer': [4, 106, 119, 107],
    'Actor': [4, 106, 107, 114, 137],
    'Biochemist': [1, 102, 107, 112, 141],
    'Orthodontist': [1, 109, 118, 119, 126],
    'Meteorologist': [1, 3, 112, 125, 118],
    'Flight Attendant': [4, 106, 109, 123, 134],
    'Archaeologist': [1, 3, 102, 113, 141],
    'Speech Writer': [4, 106, 109, 123, 114],
    'Flight Instructor': [1, 102, 106, 134, 141],
    'Probation Officer': [1, 4, 101, 123, 109],
    'Veterinary Technician': [2, 109, 118, 119, 126, 142],
    'Personal Trainer': [2, 4, 5, 109, 118, 119, 126],
    'Phlebotomist': [2, 109, 118, 119, 126],
    'Forensic Scientist': [1, 102, 103, 112, 141],
    'Landscape Architect': [4, 102, 107, 132, 110, 111, 116],
    'Physical Therapist': [1, 2, 109, 118, 119, 126],
    'Technical Writer': [4, 106, 110, 101],
    'Sound Engineer': [4, 104, 106, 110, 114],
    'Medical Illustrator': [1, 102, 103, 110, 114],
    'Museum Curator': [1, 4, 101, 123, 109],
    'Glass Blower': [4, 101, 106, 107],
    'Ranger': [2, 3, 112, 141, 147],
    'Public Relations Specialist': [4, 106, 114, 123, 109],
    'Child Psychologist': [1, 4, 101, 118, 119, 126],
    'Translator': [4, 101, 141, 123],
    'Geographer': [1, 3, 102, 103, 112, 141],
    'Clinical Psychologist': [1, 4, 101, 118, 119, 126],
    'Jewelry Designer': [4, 101, 110, 107, 123],
    'Social Media Influencer': [4, 101, 123, 109],
    'Ethical Hacker': [1, 102, 106, 101],
    'App Developer': [4, 102, 117, 106, 103, 101],
    'Audiologist': [1, 109, 118, 119, 126],
    'Optometrist': [1, 109, 118, 119, 126],
    'Speech Pathologist': [1, 109, 118, 119, 126],
    'Criminal Investigator': [1, 4, 113, 145, 109],
    'Forensic Accountant': [1, 4, 102, 140, 145, 111, 119],
    'Urban Planner': [1, 3, 102, 132, 110, 111, 138],
    'Fashion Buyer': [4, 101, 107, 110, 123, 108],
    'Choreographer': [4, 106, 107, 119],
    'Personal Chef': [2, 4, 5, 107, 130, 110, 123, 109],
    'Public Health Analyst': [1, 3, 5, 109, 118, 119, 126],
    'Sports Agent': [1, 4, 105, 106, 109, 123],
    'Fashion Blogger': [4, 101, 123, 109, 108],
    'Forensic Psychologist': [1, 4, 113, 145, 109],
    'Art Therapist': [1, 4, 101, 106, 123, 109],
    'Speech Coach': [4, 106, 109, 123],
    'Cryptographer': [1, 102, 106, 101],
    'Biomedical Scientist': [1, 102, 107, 112, 141],
    'Clinical Lab Technician': [2, 109, 118, 119, 126],
    'Music Therapist': [1, 4, 104, 106, 109, 123],
    'Technical Illustrator': [1, 102, 103, 106, 110, 101],
    'Mortician': [1, 4, 106, 109, 123],
    'Robotics Engineer': [1, 102, 107, 141],
    'Speech Scientist': [1, 109, 118, 119, 126],
    'Tattoo Artist': [4, 106, 107, 110, 101],
    'Social Worker': [1, 4, 101, 123, 109],
    'Personal Shopper': [4, 101, 107, 123],
    'Environmental Scientist': [1, 3, 112, 125, 111, 147, 141, 118],
    'FBI Agent': [1, 4, 105, 106, 139, 145],
    'Radiation Therapist': [1, 109, 118, 119, 126],
    'Dental Hygienist': [1, 109, 118, 119, 126],
    'Audiobook Narrator': [4, 106, 109, 123, 101],
    'Astronomer': [1, 102, 103, 125, 118],
    'Nuclear Physicist': [1, 102, 103, 125, 118],
    'Forensic Pathologist': [1, 4, 106, 109, 123, 113],
    'Ethnobotanist': [1, 3, 112, 141, 146, 148],
    'Cartographer': [1, 3, 102, 132, 110, 141],
    'Neuroscientist': [1, 102, 103, 118, 119, 126],
    'Genetic Counselor': [1, 102, 103, 118, 119, 126],
    'Robotics Technician': [2, 3, 102, 107, 141],
    'Crime Scene Investigator': [1, 4, 106, 109, 123, 113],
    'Ethical Hacker': [1, 102, 106, 101],
    'Cryptographer': [1, 102, 106, 101],
    'Astronaut': [1, 3, 102, 112, 125, 106, 110, 134],
    'Fine Artist': [4, 101, 106, 110, 114],
    'Florist': [4, 107, 110, 123, 109],
    'Wedding Planner': [4, 101, 107, 114, 123, 109],
    'Film Director': [4, 106, 109, 114, 123],
    'Automotive Engineer': [1, 2, 102, 107, 141],
    'Veterinary Surgeon': [1, 109, 118, 119, 126, 142],
    'Wildlife Biologist': [1, 3, 112, 118, 125],
    'Music Producer': [4, 104, 106, 109, 114],
    'Librarian': [1, 4, 101, 123, 109],
    'Audio Engineer': [4, 104, 106, 109, 110],
    'Biomedical Engineer': [1, 102, 107, 127, 141],
    'Food Scientist': [1, 109, 118, 119, 126, 130],
    'Forensic Toxicologist': [1, 109, 118, 119, 126, 113],
    'Fashion Illustrator': [4, 101, 107, 110, 114],
    'Bioinformatics Specialist': [1, 102, 107, 141],
    'Agricultural Scientist': [1, 3, 112, 141, 146, 148],
    'Astrophysicist': [1, 102, 103, 125, 118],
    'Furniture Designer': [4, 101, 107, 110, 128],
    'Jeweler': [4, 101, 110, 107],
    'Makeup Artist': [4, 101, 106, 107],
    'Forensic Anthropologist': [1, 4, 113, 145, 109],
    'Tutor': [1, 4, 144, 123, 113, 148, 136, 141, 107],
    'Corporate Trainer': [1, 4, 144, 123, 113, 148, 136, 141, 107],
    'Biomedical Technician': [2, 109, 118, 119, 126, 141],
    'Public Health Nurse': [1, 2, 3, 5, 109, 118, 119, 126, 142],
    'Forensic Psychologist': [1, 4, 113, 145, 109],
    'Fashion Merchandiser': [4, 101, 107, 110, 123, 108],
    'Cartoonist': [4, 101, 110, 107, 131],
    'Medical Examiner': [1, 4, 106, 109, 123, 113],
    'Urban Designer': [4, 101, 107, 110, 111, 132],
    'Botanist': [1, 3, 112, 141, 146, 148],
    'Ecologist': [1, 3, 112, 141, 146, 148],
    'Marine Engineer': [1, 2, 102, 107, 141],
    'Meteorologist': [1, 3, 112, 125, 118],
    'Industrial Designer': [4, 101, 107, 110, 111, 116],
    'Digital Marketing Specialist': [1, 4, 114, 123, 124, 111, 109],
    'Bioinformatics Scientist': [1, 102, 107, 141],
    'Orthopedic Surgeon': [1, 109, 118, 119, 126],
    'Environmental Health Specialist': [1, 3, 112, 141, 146, 148],
    'Physical Education Teacher': [1, 4, 5, 144, 123, 113, 148, 136, 141, 107],
    'Green Architect': [1, 4, 102, 127, 132, 110, 111, 116],
    'Conservationist': [1, 3, 112, 141, 146, 148],
    'Air Quality Analyst': [1, 3, 112, 141, 146, 148],
    'Oceanographer': [1, 3, 112, 141, 146, 148],
    'Neurosurgeon': [1, 109, 118, 119, 126],
    'Wildlife Photographer': [4, 101, 110, 114, 123],
    'Criminal Profiler': [1, 4, 113, 145, 109],
    'Ecological Economist': [1, 4, 102, 140, 145, 111, 119],
    'Behavioral Analyst': [1, 4, 101, 118, 119, 126],
    'Water Resource Engineer': [1, 2, 102, 107, 141],
    'Waste Management Specialist': [1, 3, 112, 141, 146, 148],
    'Urban Forester': [1, 3, 112, 141, 146, 148],
    'Toxicologist': [1, 102, 107, 112, 141],
    'Solar Energy Technician': [2, 3, 102, 107, 141],
    'Soil Conservationist': [1, 3, 112, 141, 146, 148],
    'River Guide': [2, 3, 107, 111, 147],
    'Renewable Energy Consultant': [1, 102, 107, 141],
    'Recycling Coordinator': [1, 3, 112, 141, 146, 148]
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

def eliminate_options(responses: list, options: dict) -> tuple[list, list]:
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

def sort_by_interest(met_criteria:list, not_met:list, careers:dict, interests:list) -> tuple:
    interest_count = {}
    if len(met_criteria) > 1:
       for i in met_criteria:
           interest_count.update({i:0})
    else:
        for i in met_criteria:
            interest_count.update({i:1})
        for i in range(3-len(met_criteria)):
            interest_count.update({not_met.pop():0})
    for i in range(len(list(interest_count.keys()))):
        for j in range(len(interests)):
            if interests[j] in careers[list(interest_count.keys())[i]]:
                interest_count[list(interest_count.keys())[i]] += 1
    sorted_interests = sorted(interest_count.items(), key=lambda x: x[1])
    return ((sorted_interests)[-1][0], (sorted_interests)[-2][0])

def get_career_recommendations(responses: list, interests: list, careers: dict) -> tuple:
    return sort_by_interest(eliminate_options(responses, careers)[0], eliminate_options(responses, careers)[1], careers, interests)

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
            interests = [INTERESTS[i] for i in interests]
            response_numbers = []
            for i in range(len(responses)):
                if not responses[i]:
                    response_numbers.append(i + 1)
            reccomendations = get_career_recommendations(response_numbers, interests, CAREER_OPTIONS)
            st.write(f'We recommend you further explore {reccomendations[0]} or {reccomendations[1]}.')