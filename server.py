from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get("textToAnalyze")


    emotions = emotion_detector(text)

    dominant_emotion = emotions["dominant_emotion"]

    if not dominant_emotion:
        return "Invalid text! Please try again!."

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    res = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    return res

   