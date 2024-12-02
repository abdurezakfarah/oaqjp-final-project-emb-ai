"""
Flask server for emotion detection using a custom EmotionDetection module.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page.
    """
    return render_template("index.html")

@app.route("/emotion_detector")
def emotion_detector_route():
    """
    Analyze the emotions of the provided text and return the results.
    """
    text = request.args.get("textToAnalyze")
    if not text:
        return "Invalid text! Please provide text to analyze."

    emotions = emotion_detector(text)

    dominant_emotion = emotions.get("dominant_emotion")
    if not dominant_emotion:
        return "Invalid text! Please try again."

    anger = emotions.get("anger", 0.0)
    disgust = emotions.get("disgust", 0.0)
    fear = emotions.get("fear", 0.0)
    joy = emotions.get("joy", 0.0)
    sadness = emotions.get("sadness", 0.0)

    res = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return res
