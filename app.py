import gzip
import pickle
import pandas as pd
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# --- Load Data ---
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with gzip.open('similarity.pkl.gz', 'rb') as f:
  similarity = pickle.load(f)


# Create a robust HTTP Session with automatic retries
def get_session():
  session = requests.Session()
  retries = Retry(
      total=3,
      backoff_factor=1,
      status_forcelist=[429, 500, 502, 503, 504],
      raise_on_status=False,
  )
  adapter = HTTPAdapter(max_retries=retries)
  session.mount('https://', adapter)
  session.mount('http://', adapter)
  return session


session = get_session()


# Cache the API responses so fetching is fast and rate-limits are avoided
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
  headers = {
      'User-Agent': (
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      )
  }

  try:
    response = session.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
      data = response.json()
      if 'poster_path' in data and data['poster_path']:
        return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
  except Exception as e:
    print(f'Error fetching poster for movie ID {movie_id}: {e}')

  return 'https://via.placeholder.com/500x750?text=No+Poster'


def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(
      list(enumerate(distances)), reverse=True, key=lambda x: x[1]
  )[1:6]

  recommended_movies = []
  recommended_movies_posters = []

  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))

  return recommended_movies, recommended_movies_posters


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select an movie then this system will gives you top 5 related movies which'
    ' you selected.',
    movies['title'].values,
)

if st.button('Predict'):
  names, posters = recommend(selected_movie_name)

  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
    st.text(names[0])
    st.image(posters[0])

  with col2:
    st.text(names[1])
    st.image(posters[1])

  with col3:
    st.text(names[2])
    st.image(posters[2])

  with col4:
    st.text(names[3])
    st.image(posters[3])

  with col5:
    st.text(names[4])
    st.image(posters[4])

# ---Footer ---
footer_css = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0e1117;
    color: #fafafa;
    text-align: center;
    padding: 8px 0px;
    font-size: 14px;
    border-top: 1px solid #262730;
    z-index: 100;
}
</style>
<div class="footer">
    <p style="margin:0;">🚀 Powered by Streamlit & TMDB | Developed by Anuj NITRR</p>
</div>
"""

st.markdown(footer_css, unsafe_allow_html=True)