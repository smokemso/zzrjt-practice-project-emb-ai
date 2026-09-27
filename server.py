"""
This module provides functionalities for emotion detection using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    raw_response = emotion_detector(text_to_analyze)
    response = emotion_predictor(raw_response)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
