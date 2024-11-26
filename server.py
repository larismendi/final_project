"""
This is the server file for the EmotionDetection web application.
It handles routes for the app, processes the input text to detect emotions,
and returns the emotion data and response message.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html template when the user visits the root URL.
    
    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handles the request to process the input text for emotion detection.
    
    Retrieves the 'textToAnalyze' query parameter, passes it to the emotion_detector 
    function, and returns the processed emotion data or an error message.
    
    Returns:
        Response: A JSON response containing the emotion data or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    emotion_data = emotion_detector(text_to_analyze)

    if emotion_data['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = emotion_data['anger']
    disgust = emotion_data['disgust']
    fear = emotion_data['fear']
    joy = emotion_data['joy']
    sadness = emotion_data['sadness']
    dominant_emotion = emotion_data['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
