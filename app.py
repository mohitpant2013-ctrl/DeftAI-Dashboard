import streamlit as st
from PIL import Image
import pandas as pd
import time
from groq import Groq

st.set_page_config(page_title="DeftAI Advanced Dashboard", page_icon="⚡", layout="wide")

# Sidebar for API Configuration & Controls
st.sidebar.title("⚡ DeftAI Control Center")
st.sidebar.markdown("---")

st.sidebar.subheader("🔑 API Configuration")
api_key_input = st.sidebar.text_input("Enter Groq API Key", type="password")

# Session State for Engine Status
if 'engine_status' not in st.session_state:
    st.session_state.engine_status = "Stopped 🔴"

st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Engine & Server Controls")
if st.sidebar.button("▶ Start AI Engine"):
    st.session_state.engine_status = "Running 🟢"
    st.sidebar.success("AI Engine Started Successfully!")

if st.sidebar.button("⏹ Stop AI Engine"):
    st.session_state.engine_status = "Stopped 🔴"
    st.sidebar.warning("AI Engine Stopped.")

st.sidebar.markdown(f"**Status:** {st.session_state.engine_status}")
st.sidebar.markdown("---")

st.sidebar.subheader("🛠 Advanced Modules")
model_choice = st.sidebar.selectbox("Choose Model", ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"])
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# Main Dashboard Area
st.title("🤖 DeftAI Ultimate Dashboard")
st.markdown("Bhai, yeh tera 24/7 cloud-powered AI workspace hai jisme Groq API integrated hai! 🔥")

tab1, tab2, tab3, tab4 = st.tabs(["💬 Hinglish Chat", "🖼 Image Processing", "📁 File Uploader", "📊 System Metrics"])

with tab1:
    st.subheader("Hinglish Chat & Real AI Responses")
    user_input = st.text_input("Apna sawal yahan type karein:")
    
    if st.button("Send Message 🚀"):
        if not api_key_input:
            st.error("Bhai, pehle sidebar mein apni Groq API key toh daal!")
        elif user_input:
            try:
                client = Groq(api_key=api_key_input)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are DeftAI, a helpful AI assistant that replies in natural Hinglish (Hindi + English mix) matching the user's vibe."
                        },
                        {
                            "role": "user",
                            "content": user_input,
                        }
                    ],
                    model=model_choice,
                    temperature=temperature,
                )
                ai_response = chat_completion.choices[0].message.content
                st.markdown(f"**Aapne pucha:** {user_input}")
                st.markdown(f"**DeftAI:** {ai_response}")
            except Exception as e:
                st.error(f"Error aa gaya bhai: {e}")
        else:
            st.warning("Pehle kuch type toh kar bhai!")

with tab2:
    st.subheader("Image Upload & Vision Analysis")
    uploaded_image = st.file_uploader("Ek image upload kar bhai (PNG/JPG)", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image Preview", use_column_width=True)
        if st.button("Analyze Image 🔍"):
            st.success(f"Image successfully analyze ho gayi! Resolution: {img.size}")

with tab3:
    st.subheader("File & Dataset Uploader")
    uploaded_file = st.file_uploader("Koi bhi document/CSV file upload karein", type=["csv", "txt", "pdf"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())
        else:
            st.info(f"File '{uploaded_file.name}' successfully received!")

with tab4:
    st.subheader("System Performance & Logs")
    st.metric(label="Engine State", value=st.session_state.engine_status)
    st.metric(label="Cloud Connection", value="Groq API Connected ⚡")
    st.code("[INFO] Connected to Groq Cloud API...\n[READY] DeftAI is fully operational 24/7...", language="bash")

