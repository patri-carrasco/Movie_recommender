from config.configuration import conn 


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
  #query = f"SELECT genre FROM title_movies WHERE genre LIKE '%Action%';" #comprobar que hay mas géneros que contengan Action
  query = f"SELECT title,avg_vote FROM title_movies WHERE genre = '{genre}' order by avg_vote DESC;"
  
  film = list(conn.execute(query))
  while cont <= 7:
    film_dict.append({
      'title': film[cont][0],
      'rating': film[cont][1]
      #trailer 
    })
    
    cont+=1
    
  
  return film_dict


def get_title(title):
  """
      Función que dado un tipo de título de película devuleva el de género con más ratings
      arg:
        genre = genero de la película
      return:
       film = titulo película
  """
   
  film_dict = {}

  query = f"SELECT genre FROM title_movies WHERE title = '{title}';"
  
  genre = list(conn.execute(query))
  print(f' fkgjaflñkga {genre[0][0]}')
  film_dict = get_genre(genre[0][0])
  
  return film_dict
