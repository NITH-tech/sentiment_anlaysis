from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    sentence = request.form['sentence']
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(sentence)

    return render_template('result.html', sentence=sentence, sentiment_scores=sentiment_scores)

if __name__ == '__main__':
    app.run(debug=True)
