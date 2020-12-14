from config.configuration import conn 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def clean_data_recommender():
    #Cargamos lo datos de IMDb movies.csv
    data = pd.read_csv("./data/IMDb movies.csv",low_memory=False)

    # Borramos columnas innecesarias
    data = data.drop(['usa_gross_income', 'worlwide_gross_income','metascore','reviews_from_users','reviews_from_critics'], axis=1)
    data = data.drop(['production_company','budget','production_company','writer'],axis = 1)

    #También borramos todos los datos nulos de las columnas. 
    data = data.dropna(subset=['actors', 'country','language','director','description'])

    #Quitamos las películas del país India
    data = data.drop(data[data['country']=='India'].index)


    # películas a partir de los años 1960
    data = data.drop(data[data['year'] < '1960'].index)


    # películas de ratings superior a 6.7
    data = data.drop(data[data['avg_vote'] < 6.7].index)



    data.reset_index(inplace=True, drop=True)

    # Guardamos los datos
    data.to_csv("../data/data.csv")