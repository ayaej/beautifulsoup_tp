from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import re

app = Flask(__name__)
CORS(app)

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tp_bs4"]
articles_col = db["articles"]

@app.route("/articles", methods=["GET"])
def get_articles():
    query = {}

    # Filtres possibles
    title = request.args.get("title")
    author = request.args.get("author")
    subcategory = request.args.get("subcategory")
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")

    if title:
        query["title"] = {"$regex": re.escape(title), "$options": "i"}

    if author:
        query["author"] = {"$regex": re.escape(author), "$options": "i"}

    if subcategory:
        query["subcategory"] = {"$regex": re.escape(subcategory), "$options": "i"}

    if start_date and end_date:
        query["date"] = {"$gte": start_date, "$lte": end_date}
    elif start_date:
        query["date"] = {"$gte": start_date}
    elif end_date:
        query["date"] = {"$lte": end_date}

    articles = list(articles_col.find(query, {"_id": 0}))
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
