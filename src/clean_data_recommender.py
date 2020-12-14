from config.configuration import conn 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#Cargamos lo datos de IMDb movies.csv
data = pd.read_csv("./data/IMDb movies.csv",low_memory=False)

# Borramos columnas innecesarias
data = data.drop(['usa_gross_income', 'worlwide_gross_income','metascore','reviews_from_users','reviews_from_critics'], axis=1)
data = data.drop(['production_company','budget','production_company','writer'],axis = 1)

#También borramos todos los datos nulos de las columnas. 
data = data.dropna(subset=['actors', 'country','language','director','description'])

# Nos quedamos sólo con el país  USA
data_usa = data[data.country == 'USA']

# Mejor ratings mayor que 6
data_usa_best = data_usa[data_usa.avg_vote > 6]

# Guardamos los datos
data_usa_best.to_csv("../data/data_usa_best.csv")