"""
Flask web application for detecting emotions in text input.
It receives user-provided text, processes it through the emotion detection
function, and returns individual emotion scores along with the dominant emotion.
This module also serves the main HTML interface for interacting with the app.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the text provided in the request and calculate the emotion scores.
    The function identifies the dominant emotion based on the highest score.
    Returns a formatted response containing all emotion values.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main HTML page for the application.
    This page acts as the user interface for submitting text to the emotion detector.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
