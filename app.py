import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from eligibility import calculate_eligibility_score
from prompts import build_prompt

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="IntelliVisa AI", page_icon="🌍")

st.title("🌍 IntelliVisa – AI Immigration Assistant")
st.markdown("Your Smart Visa Guidance Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask about any visa requirements..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    full_prompt = build_prompt(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can change model
        messages=[
            {"role": "system", "content": "You are an expert immigration assistant."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.4
    )

    ai_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.markdown(ai_reply)


# -------------------------
# Eligibility Score Section
# -------------------------

st.divider()
st.subheader("🧠 Smart Visa Eligibility Analyzer")

country = st.text_input("Country")
visa_type = st.text_input("Visa Type")
education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
funds = st.number_input("Available Funds (USD)", min_value=0)
travel_history = st.selectbox("Previous Travel History", ["None", "Some", "Frequent"])

if st.button("Check Eligibility"):

    score, feedback = calculate_eligibility_score(
        education, funds, travel_history
    )

    st.success(f"Visa Readiness Score: {score}%")
    st.write(feedback)
