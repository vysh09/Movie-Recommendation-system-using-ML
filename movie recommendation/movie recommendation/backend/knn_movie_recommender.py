import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
df = pd.read_csv("movies_with_ratings.csv")

# Combine title and genre for feature generation
df['combined_features'] = df['title'] + " " + df['genre']

# Vectorize combined features
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# Fit KNN model
knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
knn_model.fit(feature_matrix)

def get_similar_movies(title):
    if title not in df['title'].values:
        return []
    idx = df[df['title'] == title].index[0]
    distances, indices = knn_model.kneighbors(feature_matrix[idx], n_neighbors=6)
    results = []
    for i in indices[0][1:]:  # Skip the movie itself
        movie = df.iloc[i]
        results.append({
            "title": movie["title"],
            "genre": movie["genre"],
            "poster": movie["poster"],
            "rating": movie["rating"]
        })
    return results
