import pandas as pd
import streamlit as st
import pickle
import requests


headers = {
    "accept": "application/json",
    "Authorization": "Bearer 725522a1ba16147fc6098adc7be782eb"
}

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=725522a1ba16147fc6098adc7be782eb")
    data = response.json()
    pp = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500{pp}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended,recommended_movies_poster



movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movies = st.selectbox('Choose your favourite movie', movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movies)

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

