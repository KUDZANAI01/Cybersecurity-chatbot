# Cybersecurity-chatbot

This repository contains a cybersecurity chatbot called CYBERFRIDAY.

## Features
- Password strength analysis
- Phishing indicator detection
- Log analysis for suspicious activity
- Incident response guidance
- Optional OpenAI-compatible API support

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python cybersecurity_chatbot.py
```

Add your OpenAI API key to `.env` if you want AI-powered responses.

## Example interactions

```text
You: hello
CYBERFRIDAY: Hello. I am CYBERFRIDAY, your cybersecurity assistant.

You: password MyPassword123!
CYBERFRIDAY: Strong: Good length and complexity.

You: phishing Urgent! Your account has been suspended. Click here to verify your credentials.
CYBERFRIDAY: Possible phishing attempt detected. Risk indicators: urgency language, credential harvesting language, potentially insecure URL.

You: log Failed password for admin from 192.168.1.10
CYBERFRIDAY: Possible brute-force or credential attack. Block the source if unauthorized and review login logs.
```
