# 🎬 Movie Recommendation System

## 📌 Overview

This project is a **Movie Recommendation System** that suggests similar movies based on user input using **content-based filtering techniques**. It analyzes movie features like genres, cast, crew, and keywords to recommend relevant movies.

---

## 🚀 Features

* 🎯 Recommend similar movies instantly
* 🧠 Content-based filtering using cosine similarity
* 🌐 Interactive web app using Streamlit
* ⚡ Fast and simple user interface

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📊 Dataset

* TMDB 5000 Movies Dataset:
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

> ⚠️ Dataset is not included in this repository due to size limitations. Please download it manually from Kaggle.

---

## ⚙️ How It Works

1. Data preprocessing and cleaning
2. Feature extraction (genres, cast, keywords, etc.)
3. Convert text data into vectors
4. Calculate similarity using cosine similarity
5. Recommend top similar movies

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

* Add collaborative filtering
* Improve recommendation accuracy
* Deploy the app online (Streamlit Cloud / Heroku)
* Add movie posters using API

---

## 🙌 Acknowledgements

* TMDB Dataset from Kaggle
* Scikit-learn for ML tools
* Streamlit for web app framework
