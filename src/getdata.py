from config.configuration import conn 


def get_genre(genre):
  """
      
      arg:
        genre = genero de la película
      return:
       film = titulo película
  """
  print(f'dentro de ger_genre {genre}')  
  film_dict = {}
  query = "SELECT title,avg_vote FROM title_movies 	WHERE genre = 'Action' order by avg_vote DESC;"
  film = list(conn.execute(query))[0]
  film_dict['film']= film[0]
  film_dict['ratings'] = film[1]
  print(film_dict)  
  return film_dict
