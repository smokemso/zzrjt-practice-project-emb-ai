# Emotion Detection Application

This is a Flask-based web application that uses the Watson NLP EmotionPredict API to detect emotions in text.

It analyzes the provided text for the following emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

The application then identifies the **dominant emotion** from the input text.

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/smokemso/zzrjt-practice-project-emb-ai.git
cd zzrjt-practice-project-emb-ai
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python3 server.py
```

4. Access the application:
Open your web browser and visit `http://localhost:5000`.
