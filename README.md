# 🎬 Movie Recommendation System

An end-to-end Movie Recommendation application that predicts and recommends similar titles based on movie feature similarity using the K-Nearest Neighbors (KNN) algorithm. The project includes a Python-based backend service and an interactive web interface.

---

## 📌 Features

- **Content-Based Filtering**: Recommends movies using item feature similarity and metric distances via K-Nearest Neighbors.
- **RESTful Backend API**: Built using Python to process user requests and compute top-N similar movie recommendations dynamically.
- **Interactive User Interface**: A responsive frontend for querying titles and viewing recommendations with poster previews.
- **Curated Dataset**: Preprocessed metadata and ratings (`movies_with_ratings.csv`) for fast inference and query resolution.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask / FastAPI
- **Machine Learning**: Scikit-Learn (K-Nearest Neighbors), NumPy, Pandas
- **Frontend**: HTML5, CSS3, JavaScript
- **Data & Media**: CSV dataset, WebP/JPEG asset processing

---

## 📂 Project Structure

```text
movie-recommendation/
├── backend/
│   ├── app.py                      # Application server and API routing
│   ├── knn_movie_recommender.py    # KNN algorithm and feature extraction logic
│   ├── movies_with_ratings.csv     # Movie dataset with feature matrix & ratings
│   └── assets/                     # Preview images and media assets
├── frontend/
│   ├── index.html                  # Main UI layout
│   ├── style.css                   # Styling and layout
│   └── script.js                   # Client-side API integration
├── requirements.txt                # Python environment dependencies
└── README.md
