from config.configuration import conn 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("../data/IMDb movies.csv",low_memory=False)
