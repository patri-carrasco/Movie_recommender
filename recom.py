from config.configuration import conn 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("./data/IMDb movies.csv",low_memory=False)


data = data.drop(['usa_gross_income', 'worlwide_gross_income','metascore','reviews_from_users','reviews_from_critics'], axis=1)
data = data.drop(['production_company','budget','production_company','writer'],axis = 1)



print(data.description.head(3))

tfidf = TfidfVectorizer(stop_words='english')

data['description'] = data['description'].fillna('')

tfidf_matrix = tfidf.fit_transform(data['description'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

print(cosine_sim[1])