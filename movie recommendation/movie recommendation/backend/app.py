from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from knn_movie_recommender import get_similar_movies

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# Load movie data
movies_df = pd.read_csv("movies_with_ratings.csv")

@app.route("/")
def index():
    return "Movie Recommendation Backend is Running"

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    genre = data.get("genre")
    filtered = movies_df[movies_df["genre"].str.lower() == genre.lower()]
    recommendations = filtered.sample(min(10, len(filtered))).to_dict(orient="records")
    return jsonify({"recommendations": recommendations})

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "").lower()
    results = movies_df[movies_df["title"].str.lower().str.contains(query) | 
                        movies_df["genre"].str.lower().str.contains(query)]
    return jsonify({"results": results.to_dict(orient="records")})

@app.route("/knn", methods=["POST"])
def knn():
    data = request.get_json()
    title = data.get("title", "")
    similar = get_similar_movies(title)
    if not similar:
        return jsonify({"error": "Movie not found"}), 404
    return jsonify({"recommendations": similar})

if __name__ == "__main__":
    app.run(debug=True)
