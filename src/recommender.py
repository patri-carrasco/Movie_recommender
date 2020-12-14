
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import  src.clean_data_recommender as cl

#Añadimos los datos para analizar con el recommendador

def get_recommendations(title):
  
  try:
    data = pd.read_csv("./data/data_ratings.csv",low_memory=False)
  except:
    cl.clean_data_recommender
    data = pd.read_csv("./data/data_best_ratings.csv",low_memory=False)

 
  tfidf = TfidfVectorizer(stop_words='english')
  
  #Construimos la matrix TF-IDF
  tfidf_matrix = tfidf.fit_transform(data['description'])
  
  #Cosine similarity
  cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
  

  #Construir un mapa inverso de índices y títulos de películas
  indices = pd.Series(data.index, index=data['original_title']).drop_duplicates()

  # Obtenemos el índice de la película que coincide con el título
  idx = indices[title]
  
  # Obtenemos las puntuaciones de similitud por pares de todas las películas con esa película
  sim_scores = list(enumerate(cosine_sim[idx]))
  
    
  # Ordenamos las películas según las puntuaciones de similitud
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  # Obtemos las puntuaciones de las 10 películas más similares
  sim_scores = sim_scores[1:11]

  # Obtenemos los índices de películas
  movie_indices = [i[0] for i in sim_scores]

  titles_dict = []
  for i in movie_indices:
      titles_dict.append({
          'title': data['original_title'].iloc[i]
      })
  
  # Devolvemos las 10 películas más similares
  return titles_dict

  
