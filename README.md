# Recomendador de películas.




# Recomendador
Por limitaciones técnicas del equipo con el que estoy trabajando no podemos tratar con todos los datos del archivo IMDb movies.csv. Por esto vamos a tener que limitar los datos. 
Vamos a ir contando como eliminamos los datos hasta llegar a ese número de películas. 

1 .- En la primera líneas de código borramos las columnas que no necesitamos para hacer el recomendador:  
~~~
usa_gross_income, worlwide_gross_income,
metascore,
reviews_from_users,reviews_from_critics, production_company,
budget,
production_company,
writer
~~~

2 .- También borramos todos los datos nulos de las columnas. 
~~~
data = data.dropna(subset=['actors', 'country','language','director','description'])
~~~

3.- Nos quedamos con las películas americanas 
~~~
data_usa = data[data.country == 'USA']
~~~

4.- Y  que tengan una ratings mayor que 6.
~~~
data_usa_best = data_usa[data_usa.avg_vote > 6]
~~~

