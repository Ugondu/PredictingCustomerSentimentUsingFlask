from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# creating flask app

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/process', methods =['POST'])
def analyze_text():
    text = request.form["text"]
    score = analyzer.polarity_scores(text)['compound']
    
    if score > 0:
        sentiment = "Positive Comment"
    elif score == 0:
        sentiment = "Neutral comment"
    else:
        sentiment = "Negative comment"
    
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(port=5002, debug=True)