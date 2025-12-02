import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotion_and_scores = formatted_response["emotionPredictions"][0]["emotion"]
    anger_score = emotion_and_scores["anger"]
    disgust_score = emotion_and_scores["disgust"]
    fear_score = emotion_and_scores["fear"]
    joy_score = emotion_and_scores["joy"]
    sadness_score = emotion_and_scores["sadness"]

    max_score = max(emotion_and_scores.values())

    for _emotion,_score in emotion_and_scores.items():
        if _score == max_score:
            dominant_emotion = _emotion

    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }