from config.configuration import conn 


def get_genre(genre):
  """
      
      arg:
        genre = genero de la película
      return:
       film = titulo película
  """
   
  film_dict = {}
  query = f"SELECT title,avg_vote FROM title_movies WHERE genre = '{genre}' order by avg_vote DESC;"
  film = list(conn.execute(query))[0]
  film_dict['film']= film[0]
  film_dict['ratings'] = film[1]
  
  return film_dict
