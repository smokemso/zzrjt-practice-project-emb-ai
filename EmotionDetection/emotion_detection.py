import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)  
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotion_predictions = formatted_response.get("emotionPredictions", [])
        emotion_values = [prediction.get("emotion", {}) for prediction in emotion_predictions]
        highest_emotion = max(emotion_values[0], key=emotion_values[0].get)
        emotion_dict = emotion_values[0]
        emotion_dict['Dominant'] = highest_emotion
    elif response.status_code == 400:
        emotion_dict = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'Dominant': None}
        
    # Returning a dictionary containing emotion_detector results
    return emotion_dict
