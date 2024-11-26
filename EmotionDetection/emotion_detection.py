import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function uses the Watson NLP Emotion Predict API to analyze emotions in a given text.
    
    Args:
    text_to_analyze (str): The text to be analyzed for emotions.
    
    Returns:
    dict: The 'text' attribute of the response object containing emotion analysis results.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        response_data = response.json()

        emotion_scores = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        anger = emotion_scores.get('anger', 0.0)
        disgust = emotion_scores.get('disgust', 0.0)
        fear = emotion_scores.get('fear', 0.0)
        joy = emotion_scores.get('joy', 0.0)
        sadness = emotion_scores.get('sadness', 0.0)
        
        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotions, key=emotions.get)
        
        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        
        return result
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
