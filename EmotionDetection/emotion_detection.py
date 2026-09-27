"""
This module provides functions to interact with the Watson NLP EmotionPredict API
and process its responses.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Calls the Watson NLP EmotionPredict API and returns the raw JSON response.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers, timeout=10)

    if response.status_code == 200:
        return json.loads(response.text)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return None

def emotion_predictor(response):
    """
    Extracts emotions and computes the dominant emotion from the raw API response.
    """
    if response is None or (
            'dominant_emotion' in response and response['dominant_emotion'] is None):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotion_predictions = response.get("emotionPredictions", [])
    if not emotion_predictions:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = emotion_predictions[0].get("emotion", {})
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': dominant_emotion
    }
