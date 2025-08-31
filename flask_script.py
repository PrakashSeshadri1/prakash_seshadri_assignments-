from flask import Flask, render_template, request, send_file, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re, time, random, io, json
from urllib.parse import quote_plus
import warnings
from flask_cors import CORS

warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app, origins=["https://preview--review-radar-77.lovable.app"])

# -------------------- Scraper Class --------------------
class GoogleReviewsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0',
            'Accept-Language': 'en-US,en;q=0.9',
        })

    def scrape_reviews_from_search(self, business_name, location="", max_reviews=200):
        reviews = []
        try:
            search_queries = [
                f"{business_name} reviews",
                f"{business_name} customer reviews",
                f"{business_name} google reviews",
            ]
            if location:
                search_queries = [f"{q} {location}" for q in search_queries]

            for query in search_queries:
                search_url = f"https://www.google.com/search?q={quote_plus(query)}&num=20"
                response = self.session.get(search_url, timeout=15)
                soup = BeautifulSoup(response.content, 'html.parser')

                review_selectors = [
                    'span.aCOpRe', 'div.VwiC3b', 'div.yXK7lf', 'div.MUxGbd',
                    'div.review-item', 'span.review-text'
                ]

                for selector in review_selectors:
                    containers = soup.select(selector)
                    for c in containers:
                        text = c.get_text().strip()
                        if self._is_valid_review(text):
                            stars = self._extract_stars_from_text(text)
                            if not any(r['text'] == text for r in reviews):
                                reviews.append({
                                    'text': text,
                                    'stars': stars,
                                    'source': 'Google Search'
                                })
                        if len(reviews) >= max_reviews:
                            return reviews
                time.sleep(random.uniform(1, 2))
            return reviews or self._get_sample_reviews(business_name, max_reviews)
        except Exception as e:
            print("Scraping failed:", e)
            return self._get_sample_reviews(business_name, max_reviews)

    def _is_valid_review(self, text):
        if len(text) < 15 or len(text) > 500: 
            return False
        blacklist = ['privacy policy', 'terms', 'contact', 'address']
        return not any(b in text.lower() for b in blacklist)

    def _extract_stars_from_text(self, text):
        match = re.search(r'(\d)/5', text)
        return int(match.group(1)) if match else 0

    def _get_sample_reviews(self, business_name, num_reviews=50):
        samples = [
            f"Great service at {business_name}, will return!",
            f"Decent experience at {business_name}.",
            f"Terrible service at {business_name}, not recommended."
        ]
        reviews = []
        for i in range(num_reviews):
            txt = random.choice(samples)
            stars = random.choice([1, 3, 5])
            reviews.append({'text': txt, 'stars': stars, 'source': 'Sample Data'})
        return reviews

# -------------------- Sentiment Analyzer --------------------
class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()

    def analyze(self, text):
        blob_score = TextBlob(text).sentiment.polarity
        vader_score = self.vader.polarity_scores(text)['compound']
        combined = (blob_score + vader_score) / 2
        if combined >= 0.1: sentiment = 'Positive'
        elif combined <= -0.1: sentiment = 'Negative'
        else: sentiment = 'Neutral'
        return {'sentiment': sentiment, 'score': combined}

# -------------------- Flask Routes --------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        business = request.form.get("business")
        location = request.form.get("location")
        max_reviews = int(request.form.get("max_reviews", 200))

        scraper = GoogleReviewsScraper()
        analyzer = SentimentAnalyzer()

        reviews = scraper.scrape_reviews_from_search(business, location, max_reviews)

        analyzed = []
        for r in reviews:
            res = analyzer.analyze(r['text'])
            r.update(res)
            analyzed.append(r)

        df = pd.DataFrame(analyzed)

        # Charts
        sentiment_counts = df['sentiment'].value_counts()
        fig_pie = px.pie(names=sentiment_counts.index, values=sentiment_counts.values,
                         title="Sentiment Distribution",
                         color=sentiment_counts.index,
                         color_discrete_map={'Positive': 'green', 'Negative': 'red', 'Neutral': 'gold'})
        pie_html = fig_pie.to_html(full_html=False)

        fig_hist = px.histogram(df, x="score", nbins=20, title="Sentiment Score Distribution")
        hist_html = fig_hist.to_html(full_html=False)

        return render_template("results.html", business=business, location=location,
                               total=len(df), table=df.to_dict(orient="records"),
                               pie_chart=pie_html, hist_chart=hist_html)
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        buf = io.BytesIO()
        df.to_csv(buf, index=False)
        buf.seek(0)
        return send_file(buf, mimetype="text/csv", as_attachment=True,
                         download_name="reviews_analysis.csv")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# -------------------- Run --------------------
if __name__ == "__main__":
    app.run(debug=True)
