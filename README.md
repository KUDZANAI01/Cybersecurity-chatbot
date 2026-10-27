# Cybersecurity-chatbot

A modern cybersecurity assistant named CYBERFRIDAY.

## Features
- Password strength analysis
- Phishing detection based on message patterns
- Suspicious log review
- Incident response playbook hints
- Streamlit dashboard for quick analysis
- Optional OpenAI-powered chat responses

## Project structure
- `cybersecurity_chatbot.py` — core logic and CLI assistant
- `app.py` — Streamlit web dashboard
- `.env.example` — environment configuration template
- `requirements.txt` — dependencies

## Run the CLI assistant

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python cybersecurity_chatbot.py
```

## Run the dashboard

```bash
streamlit run app.py
```

## Example prompts

```text
hello
password MyPassword123!
phishing Urgent! Your account has been suspended. Click here to verify your credentials.
log Failed password for admin from 192.168.1.10
report suspicious login attempts from multiple IPs
```

## Notes
- The app works in offline mode without an API key.
- Add your OpenAI key to `.env` to enable AI-generated responses.
