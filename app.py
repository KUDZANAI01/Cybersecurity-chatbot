import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from cybersecurity_chatbot import CyberSecurityAssistant

load_dotenv()

st.set_page_config(page_title="CYBERFRIDAY Dashboard", page_icon="🛡️", layout="wide")

assistant = CyberSecurityAssistant()

st.title("CYBERFRIDAY | Cybersecurity Assistant")
st.caption("AI-powered assistant for phishing detection, password checks, log review, and incident triage.")

with st.sidebar:
    st.header("Controls")
    st.markdown("### Quick actions")
    if st.button("Check Password Strength"):
        st.session_state.quick_action = "password"
    if st.button("Scan Email for Phishing"):
        st.session_state.quick_action = "phishing"
    if st.button("Review Log Entry"):
        st.session_state.quick_action = "log"
    if st.button("Incident Response Guide"):
        st.session_state.quick_action = "report"

    st.markdown("---")
    st.markdown("**Status:**")
    st.success("Assistant active")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am CYBERFRIDAY. Ask me about password checks, phishing, suspicious logs, or incident response."}
    ]

if "quick_action" not in st.session_state:
    st.session_state.quick_action = None


if st.session_state.quick_action == "password":
    st.session_state.messages.append({"role": "assistant", "content": "Please enter a password to assess:"})
    st.session_state.quick_action = None


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask CYBERFRIDAY a cybersecurity question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = assistant.generate_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Embedded risk tools
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Password Strength")
    password = st.text_input("Enter a password", type="password", key="password_check")
    if password:
        st.code(assistant.analyze_password_strength(password), language="text")

with col2:
    st.subheader("Phishing Scan")
    email_text = st.text_area("Paste email content", height=120, key="phishing_check")
    if email_text:
        st.code(assistant.analyze_phishing_email(email_text), language="text")

with col3:
    st.subheader("Log Review")
    log_text = st.text_area("Paste log line", height=120, key="log_check")
    if log_text:
        st.code(assistant.analyze_log_entry(log_text), language="text")

# Incident response summary
st.markdown("---")
st.subheader("Incident Response Generator")
incident_context = st.text_area("Describe the incident or alert context", height=100)
if incident_context:
    st.code(assistant.incident_summary(incident_context), language="text")
