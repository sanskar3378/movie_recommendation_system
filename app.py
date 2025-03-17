import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7b265889effd91ac7d8e331e33932630&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:11]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster



movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")


selected_movie_name  = st.selectbox(label = "Enter a movie name", 
                       options = movies['title'].values)

number = st.number_input("Insert a number", format="%i", step=1)

if st.button('Recommend'):
    names, posters =  recommend(selected_movie_name)
    
    cols = st.columns(3)

    for i in range(number):
        cols[i%3].write(names[i])
        cols[i%3].image(posters[i], width= 200)





