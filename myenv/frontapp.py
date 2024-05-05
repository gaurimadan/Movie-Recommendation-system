import streamlit as st
import numpy as np
import pickle

st.header("Movie Recommendation System")

new_movies = pickle.load(open(r"D:\Movie-recommender-system\artifacts\new_movies.pkl",'rb'))
similarity= pickle.load(open(r"D:\Movie-recommender-system\artifacts\similiarity.pkl",'rb'))

# def fetch_front(suggestion):
#     movie_name=[]
#     ids_index=[]
#     poster_url=[]
    
#     for movie_id in suggestion:
#         movie_name.append(new_movies.index[movie_id])

#     for name in movie_name[0]:
#         ids=np.where(new_movies["title"]==name)[0][0]
#         ids_index.append(ids)
def recommender(movie):
    movie_index = new_movies[new_movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(new_movies.iloc[i[0]].title)
    return recommended_movies

    



    
selected_books=st.selectbox(
    "Type or select book",
    new_movies["title"]
     
)
if st.button("Recommendation"):
    recommendaton_movies=recommender(selected_books)


    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
         st.text(recommendaton_movies[0])
    
    with col2:
         st.text(recommendaton_movies[1])
    
    with col3:
         st.text(recommendaton_movies[2])
    
    with col4:
         st.text(recommendaton_movies[3])
    
    with col5:
         st.text(recommendaton_movies[4])