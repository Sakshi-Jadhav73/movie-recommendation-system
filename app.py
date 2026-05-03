import pickle
import streamlit as st
import requests

# -------------------------------
# 🔑 PUT YOUR TMDB API KEY HERE
# -------------------------------
API_KEY = "YOUR_API_KEY_HERE"

# -------------------------------
# 🎬 FETCH POSTER (STABLE VERSION)
# -------------------------------
def fetch_poster(movie_name):
    try:
        url = "https://api.themoviedb.org/3/search/movie"

        params = {
            "api_key": API_KEY,
            "query": movie_name
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, params=params, headers=headers, timeout=10)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=API+Error"

        data = response.json()

        if data.get("results") and len(data["results"]) > 0:
            poster_path = data["results"][0].get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path

        return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        print("Error:", e)
        return "https://via.placeholder.com/500x750?text=Error"


# -------------------------------
# 🤖 RECOMMENDER FUNCTION
# -------------------------------
def recommender(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except:
        return [], []

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    # 🔥 Reduced API calls (important)
    for i in distances[1:4]:
        movie_name = movies.iloc[i[0]].title
        recommended_movie_names.append(movie_name)
        recommended_movie_posters.append(fetch_poster(movie_name))

    return recommended_movie_names, recommended_movie_posters


# -------------------------------
# 🎨 UI
# -------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Get similar movies instantly 🎥</h4>", unsafe_allow_html=True)

# -------------------------------
# 📂 LOAD FILES
# -------------------------------
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except:
    st.error("❌ Error loading files. Check movies.pkl & similarity.pkl")
    st.stop()

movies_list = movies['title'].values

# -------------------------------
# 🎥 SELECT MOVIE
# -------------------------------
selected_movie = st.selectbox("Select a movie:", movies_list)

# -------------------------------
# 🚀 SHOW RESULT
# -------------------------------
if st.button("Show Recommendation"):

    with st.spinner("Fetching recommendations... 🎯"):
        names, posters = recommender(selected_movie)

    if not names:
        st.error("❌ No recommendations found")
    else:
        st.markdown("## 🎥 Recommended Movies")

        cols = st.columns(len(names))

        for i in range(len(names)):
            with cols[i]:
                st.image(posters[i])
                st.caption(names[i])