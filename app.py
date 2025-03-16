import streamlit as st
import pickle
import pandas as pd

def recommend(name):
    movie_index = movies_df[movies_df['title'] == name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:11]
    ret = list()
    for i in movie_list:
        ret.append(movies_df.iloc[i[0]].title)
    return ret


st.title("Movie Recommendation System")
movie_dict = pickle.load(open('movies.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_df = pd.DataFrame(movie_dict)

selected_movie_name = st.selectbox(label='Enter a movie name',
                       options = movies_df['title'].values)

# movie_name = st.text_input(label='Enter a movie name')

if st.button('Recommend'):
    res = recommend(selected_movie_name)
    for i in res:
        st.write(i)