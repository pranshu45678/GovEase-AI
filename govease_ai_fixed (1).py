import streamlit as st
import requests


from openai import OpenAI

GNANI_API_KEY = st.secrets["GNANI_API_KEY"]
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def speech_to_text(audio_file):
    headers = {
        "x-api-key": GNANI_API_KEY
    }

    files = {
        "audio_file": audio_file
    }

    data = {
        "language_code": "en-IN",
        "format": "transcribe",
        "itn_native_numerals": "true"
    }

    response = requests.post(
        "https://api.vachana.ai/stt/v3",
        headers=headers,
        files=files,
        data=data
    )

    return response.json()




st.subheader("📄 Popular Government Documents")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    🪪 Aadhaar Card

    • Identity Proof
    • Address Proof
    • Required for most government services
    """)

    st.info("""
    🏦 PAN Card

    • Tax Identification
    • Banking & Financial Services
    """)

with col2:
    st.info("""
    🛂 Passport

    • International Travel
    • Government-issued Identity
    """)

    st.info("""
    🗳️ Voter ID

    • Voting in Elections
    • Identity Proof
    """)

with col1:
    st.markdown("### 🪪 Identity Services")
    st.markdown("[Aadhaar](https://uidai.gov.in)")
    st.markdown("[PAN Card](https://www.onlineservices.nsdl.com)")
    st.markdown("[Voter ID](https://voters.eci.gov.in)")
    st.markdown("[Passport](https://passportindia.gov.in)")

with col2:
    st.markdown("### 🚗 Transport Services")
    st.markdown("[Driving Licence](https://parivahan.gov.in)")
    st.markdown("[Vehicle Services](https://parivahan.gov.in)")
    st.markdown("[DigiLocker](https://www.digilocker.gov.in)")
    st.markdown("[UMANG](https://web.umang.gov.in)")
   

st.markdown("[PM-KISAN](https://pmkisan.gov.in)")
st.markdown("[National Scholarship Portal](https://scholarships.gov.in)")
st.markdown("[EPFO](https://www.epfindia.gov.in)")
st.markdown("[MyGov](https://www.mygov.in)")


language = st.selectbox(
    "Choose Language",
    ["English", "Hindi", "Telugu"]
)
if language == "Hindi":
    answer_language = "Answer only in Hindi."

elif language == "Telugu":
    answer_language = "Answer only in Telugu."

else:
    answer_language = "Answer only in English."
if language == "English":
    title_text = "GoVEase AI"
    services_text = "🔗 Quick Government Services"
    schemes_text = "🌾 Government Schemes"
    chatbot_text = "🤖 GovEase AI Chatbot"
    voice_text = "🎤 Voice Assistant"

    age_text = "Enter Age"
    occupation_text = "Occupation"
    question_text = "Ask your question"
    button_text = "Check Eligibility"

elif language == "Hindi":
    title_text = "गोवईज़ एआई"
    services_text = "🔗 सरकारी सेवाएं"
    schemes_text = "🌾 सरकारी योजनाएं"
    chatbot_text = "🤖 गोवईज़ एआई चैटबॉट"
    voice_text = "🎤 वॉयस असिस्टेंट"

    age_text = "आयु दर्ज करें"
    occupation_text = "पेशा"
    question_text = "अपना प्रश्न पूछें"
    button_text = "पात्रता जांचें"

else:
    title_text = "గోవీజ్ AI"
    services_text = "🔗 ప్రభుత్వ సేవలు"
    schemes_text = "🌾 ప్రభుత్వ పథకాలు"
    chatbot_text = "🤖 గోవీజ్ AI చాట్‌బాట్"
    voice_text = "🎤 వాయిస్ అసిస్టెంట్"

    age_text = "వయస్సు నమోదు చేయండి"
    occupation_text = "వృత్తి"
    question_text = "మీ ప్రశ్న అడగండి"
    button_text = "అర్హత తనిఖీ చేయండి"
st.title(title_text)
st.header(services_text)


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
# Smart Document Checklist

service_info = {
    "PAN Card": {
        "fee": "₹107",
        "time": "15-20 Days"
    },
    "Passport": {
        "fee": "₹1500",
        "time": "7-30 Days"
    },
    "Driving Licence": {
        "fee": "₹200-500",
        "time": "7-30 Days"
    },
    "Aadhaar Update": {
        "fee": "₹50",
        "time": "1-2 Weeks"
    },
    "Voter ID": {
        "fee": "Free",
        "time": "2-4 Weeks"
    }
    "Caste Certificate": {
    "fee": "₹35",
    "time": "7-15 Days"
},

"Income Certificate": {
    "fee": "₹35",
    "time": "7-15 Days"
},
}

st.header("📄 Smart Document Checklist")

service = st.selectbox(
    "Select Service",
    [
        "Aadhaar Update",
        "PAN Card",
        "Voter ID",
        "Passport",
        "Driving Licence",
        "Caste Certificate",
        "Income Certificate"
    ]
)



if service == "Aadhaar Update":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ Address Proof")
    st.write("✅ Mobile Number")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Fees and processing times are approximate and may change.")

elif service == "PAN Card":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ Passport Size Photo")
    st.write("✅ Address Proof")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Fees and processing times are approximate and may change.")

elif service == "Voter ID":
    st.success("Required Documents")
    st.write("✅ Age Proof")
    st.write("✅ Address Proof")
    st.write("✅ Passport Size Photo")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")

elif service == "Passport":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ PAN Card")
    st.write("✅ Address Proof")
    st.write("✅ Passport Size Photo")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Fees and processing times are approximate and may change.")
    
  elif service == "Caste Certificate":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ Ration Card (if available)")
    st.write("✅ Address Proof")
    st.write("✅ Passport Size Photo")
    st.write("✅ Previous Caste Certificate (if applicable)")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Requirements may vary by state.")

elif service == "Income Certificate":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ Address Proof")
    st.write("✅ Income Proof / Salary Certificate")
    st.write("✅ Ration Card (if available)")
    st.write("✅ Passport Size Photo")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Requirements may vary by state.")
    
elif service == "Driving Licence":
    st.success("Required Documents")
    st.write("✅ Aadhaar Card")
    st.write("✅ Learner Licence")
    st.write("✅ Address Proof")
    st.info(f"💰 Approximate Fee: {service_info[service]['fee']}")
    st.info(f"⏱ Estimated Time: {service_info[service]['time']}")
    st.caption("⚠️ Fees and processing times are approximate and may change.")
     
st.header("📄 Document Simplifier")

uploaded_doc = st.file_uploader(
    "Upload Government Document",
    type=["txt"]
)
if uploaded_doc:

    document_text = uploaded_doc.read().decode("utf-8")

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
                Simplify this government document into easy language.
                Respond in {language}.
                Explain only the important points.
                """
            },
            {
                "role": "user",
                "content": document_text
            }
        ]
    )

    simplified = response.choices[0].message.content

    st.subheader("📖 Simplified Version")
    st.write(simplified)

st.header(chatbot_text)

user_question = st.text_input("Ask GovEase AI")


if user_question:

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are GovEase AI, an assistant that helps Indian citizens with government schemes, Aadhaar, PAN Card, Voter ID, Driving Licence, DigiLocker, scholarships, and official government services. {answer_language}"
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    answer = response.choices[0].message.content

    st.success(answer)
    


st.header(voice_text)

audio_file = st.file_uploader(
    "Upload Voice Recording",
    type=["wav", "mp3", "m4a"]
)

if audio_file:

    st.success("Audio uploaded successfully!")
    st.write("Filename:", audio_file.name)

    result = speech_to_text(audio_file)

    transcript = result.get("transcript", "")

    st.subheader("Recognized Text")
    st.write(transcript)

    response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are GovEase AI, an assistant that helps Indian citizens with government schemes, Aadhaar, PAN Card, Voter ID, Driving Licence, DigiLocker, scholarships, and official government services."
        },
        {
            "role": "user",
            "content": transcript
        }
    ]
)

    answer = response.choices[0].message.content

    st.subheader("🤖 GovEase AI Answer")
    st.write(answer)
