# **Recomendador de películas.**

<div align="center">
  <a href="default.asp">
    <img src="https://portugalinews.eu/wp-content/uploads/2018/09/film.jpg" alt="Recommender" style="width:400px;height:400px;", aling = "center">
  </a>
</div>

# **Introducción**
  En este proyecto final vamos a hacer un recomendador de películas.

  Para ello hemos creado una API para ofrecer al cliente nuestras recomendaciones a medida que el cliente nos diga sus géneros o películas favoritas. 

# **Estructura del repo**
  Hemos estructurado el proyecto en varios archivos y carpetas para que sea más fácil su entendimiento.

  **config:** carpeta que usamos para la configuración básica del proyecto.

  **data:**  carpeta donde va los archivos datos.
  
  **css:** carpeta que contiene los achivos de css para la visualización de datos.

  **js:** carpeta que contiene los archivos js para la visualización de datos


  **src:** carpeta que guarda todos los archivos de funciones que usamos en este proyecto:
    
    * getdata.py :archivo que tiene las funciones de GET de la api para obtener los datos recomendados.
    * gettrailer.py : archivo que tiene las funciones para obtener los enlaces a los trailers de las películas.
    * clean_data_recommender.py : Limpieza y eliminación de los datos para el recomendador por las limitaciones mas abajo comentadas.
    * recommender.py : archivo que con tiene las funciones para la recomendaciones de películas con Machine Learning



**api.py:** Este es el archivo principal de la API.

**index.html:** Archivo html de las visualizaciones

**index.md:** Archivo de la documentación de la API
**Movie recommender.pdf** : Presentación del proyecto

# **Recomendador**
Por limitaciones técnicas del equipo con el que estoy trabajando no podemos tratar con todos los datos del archivo IMDb movies.csv. Por esto vamos a tener que limitar los datos. 
Vamos a ir contando como eliminamos los datos hasta llegar a ese número de películas. 

1 .- En la primera líneas de código borramos las columnas que no necesitamos para hacer el recomendador:  
~~~
usa_gross_income, worlwide_gross_income,
metascore,
reviews_from_users,reviews_from_critics, production_company,
budget,
production_company,
writer,
title
~~~

2 .- También borramos todos los datos nulos de las columnas. 
~~~
data = data.dropna(subset=['actors', 'country','language','director','description'])
~~~

3.- Borramos las películas de la India 
~~~
data = data.drop(data[data['country']=='India'].index)
~~~

4.- Y  que tengan una ratings mayor que 6.7.
~~~
data = data.drop(data[data['avg_vote'] < 6.7].index)

~~~
5.- Nos quedamos con las películas a partir de 1960
~~~
data = data.drop(data[data['year'] < '1960'].index)
~~~

## **Funcionamiento del recomendador por machine learning**

### Procesamiento del lenguaje natural. 
Para calcular las similitudes de y/o disimilitud hay que calcular los vectores de cada palabra de cada descripción. 
 

### Los vectores de palabras

Los vectores de palabras son representaciones vectorizadas de palabras en un documento. 
Los vectores llevan consigo un significado semántico. Por ejemplo, el hombre y el rey tendrán representaciones vectoriales cercanas entre sí, mientras que el hombre y la mujer tendrán representaciones alejadas entre sí.

Calcularemos los vectores de frecuencia de término-frecuencia de documento inverso (TF-IDF) para cada documento. Esto nos dará una matriz donde cada columna representa una palabra en el vocabulario general (todas las palabras que aparecen en al menos un documento), y cada columna representa una película.

Scikit-learn tiene una clase TfIdfVectorizer incorporada que produce la matriz TF-IDF.

### Matriz TF-IDF.
Eliminamos las palabras vacías como 'el', 'una', etc. ya que no brindan ninguna información útil sobre el tema;
Reemplazamos los valores que no sean un número con una cadena en blanco;
Finalmente, construimos la matriz TF-IDF sobre los datos.

### Similarity 
Dado que hemos utilizado el vectorizador TF-IDF, calcular el producto escalar entre cada vector nos dará directamente la puntuación de similitud del coseno. Por lo tanto, usaremos linear_kernel () de sklearn en lugar de cosine_similarities () ya que es más rápido.

### Construir un mapa inverso de índices y títulos de películas
Vamos a definir una función que toma el título de una película como entrada y genera una lista de las 10 películas más similares. 
En primer lugar, para esto, necesitamos un mapeo inverso de títulos de películas e índices de DataFrame. En otras palabras, necesitamos un mecanismo para identificar el índice de una película en su DataFrame de metadatos, dado su título.


# Enlaces usados
Dataset de películas https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset

Sistema de recomendador: https://www.datacamp.com/community/tutorials/recommender-systems-python

Apuntes de las clases https://github.com/sheriffff/teaching-ironhack-data-madrid-2020

Visualización https://github.com/german-alvarez-dev/data-visualization-for-data-analysts

# Tecnologías usadas

* Configuración interna

    - sys

    - json

    - load_dotenv

    - os

* Tratamiento de datos

    - pandas

    - selenium

    - sqlalchemy

    - Mysql

* Api

    - flask, Flask, request

    - flask_cors, CORS

    - markdown extensions fenced_code

* Recommender

    - sklearn.feature_extraction.text:  TfidfVectorizer

    - sklearn.metrics.pairwise:  linear_kernel
