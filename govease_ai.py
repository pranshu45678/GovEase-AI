import streamlit as st

st.title("GoVEase AI")

language = st.selectbox(
    "Choose Language",
    ["English", "Hindi", "Telugu"]
)

if language == "English":
    age_text = "Enter Age"
    occupation_text = "Occupation"
    question_text = "Ask your question"
    button_text = "Check Eligibility"
elif language == "Hindi":
    age_text = "आयु दर्ज करें"
    occupation_text = "पेशा"
    question_text = "अपना प्रश्न पूछें"
    button_text = "पात्रता जांचें"
else:
    age_text = "వయస్సు నమోదు చేయండి"
    occupation_text = "వృత్తి"
    question_text = "మీ ప్రశ్న అడగండి"
    button_text = "అర్హత తనిఖీ చేయండి"

age = st.number_input(age_text, min_value=1, max_value=120)

occupation = st.selectbox(
    occupation_text,
    ["Student", "Farmer", "Employee", "Business Owner", "Other"]
)

query = st.text_input(question_text)

state = st.selectbox(
    "Select State",
    ["Telangana", "Andhra Pradesh", "Karnataka", "Tamil Nadu"]
)

if st.button(button_text):

    if occupation == "Student":
        st.success("Eligible for Scholarship Schemes")
    elif occupation == "Farmer":
        st.success("Eligible for Farmer Welfare Schemes")
    elif occupation == "Employee":
        st.success("Eligible for Skill Development Programs")
    elif occupation == "Business Owner":
        st.success("Eligible for MSME Support Schemes")

# Form Assistant

st.header("Form Assistant")

name = st.text_input("Full Name")
aadhaar = st.text_input("Aadhaar Number")
mobile = st.text_input("Mobile Number")
address = st.text_area("Address")

st.write("Name =", name)
st.write("Aadhaar =", aadhaar)
st.write("Mobile =", mobile)
st.write("Address =", address)

if name and aadhaar and mobile and address:
    st.success("All required fields are filled")
    st.progress(100)
    st.header("🤖 GovEase AI Chatbot")

user_question = st.text_input("Ask GovEase AI")

if user_question:

    q = user_question.lower()

    if "driving license" in q:
        st.success("You can apply through the Parivahan portal.")

    elif "aadhaar" in q:
        st.success("Aadhaar is issued by UIDAI.")

    elif "farmer" in q:
        st.success("You may be eligible for farmer welfare schemes.")

    elif "scholarship" in q:
        st.success("Students may be eligible for scholarship schemes.")

    else:
        st.info("Sorry, I don't have information on that yet.")
