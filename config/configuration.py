import os
import dotenv
from sqlalchemy import create_engine, inspect

dotenv.load_dotenv()

# cargar los datos de la conexión

pasword = os.getenv("MYSQL_PWD")
user = os.getenv("MYSQL_USER")

# cargar la base de datos movies
database = 'movies'
mysql_url = f'mysql://{user}:{pasword}@localhost/{database}'

# crear la conexión con mysql
engine = create_engine(mysql_url)
conn = engine.connect()