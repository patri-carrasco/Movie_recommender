from config.configuration import conn 
import  src.gettrailer as gett
import pandas as pd

def get_genre(genre):
  """
      Función que dado un tipo de género de película da el que mejor rating tiene
      arg:
        genre = genero de la película
      return:
       film = titulo película
  """
  cont = 0 
  film_dict = []
  query = f"SELECT original_title, avg_vote FROM title_movies WHERE genre LIKE '%%{genre}%%' order by avg_vote DESC;" #comprobar que hay mas géneros que contengan Action
  #query = f"SELECT title,avg_vote FROM title_movies WHERE genre = '{genre}' order by avg_vote DESC;"
  
  film = list(conn.execute(query))
  if len(film) == 0:
    return {
      'status':500,
      'error_msg': f'Genre {genre} not found',
      'data': []
       }

  while cont <= 3:
    film_dict.append({
      'title': film[cont][0],
      'rating': film[cont][1],
      'trailer': gett.get_trailer(film[cont][0])
    })
    
    cont+=1
    
  
  return {
      'status':200 ,
      'error_msg': '',
      'data' : film_dict
       }


def get_title(title):
  """
      Función que dado un tipo de título de película devuleva el de género con más ratings
      arg:
        genre = genero de la película
      return:
       film = titulo película
  """
   
  film_dict = {}

  query = f"SELECT genre FROM title_movies WHERE original_title = '{title}';"
  
  genre = list(conn.execute(query))
  if len(genre) == 0:
    return {
      'status':500,
      'error_msg': f'Title {title} not found',
      'data': []
       }

  film_dict = get_genre(genre[0][0])
  
  return {
      'status':200 ,
      'error_msg': '',
      'data' : film_dict
       }

def get_data_visual():
  return  {
    'by_genre': get_genre_data(),
    'by_year': get_year_data(),
    'by_rating':get_rating_data()
    }

def get_genre_data():
  query = f"SELECT COUNT(original_title) as  total , genre FROM title_movies WHERE genre not like'%%,%%'  group by genre order by total DESC;"
  data = list(conn.execute(query))
  data_genre= []
  
  for i in range(0,len(data)):
    data_genre.append({
      'total':data[i][0],
      'genre':data[i][1]
    })
  return data_genre


def get_year_data():
  query = f"SELECT COUNT(original_title) as  total , year FROM title_movies where year > 2000  group by year order by year DESC;"
  data = list(conn.execute(query))
  data_year= []
  
  for i in range(0,len(data)):
    data_year.append({
      'total':data[i][0],
      'year':data[i][1]
    })
  return data_year

def get_rating_data():
  query = f"SELECT COUNT(original_title) as  total , round(avg_vote) as ratings FROM title_movies  group by ratings  order by ratings DESC;"
  data = list(conn.execute(query))
  data_rating= []
  
  for i in range(0,len(data)):
    data_rating.append({
      'total':data[i][0],
      'rating':data[i][1]
    })
  return data_rating