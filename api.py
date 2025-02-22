from flask import Flask, request

from flask import Flask, request
from flask import request
import markdown.extensions.fenced_code

import  src.getdata as get
import src.recommender  as rec

from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
  
   
  readme_file = open("index.md","r")
  md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
  return md_template_string


@app.route("/genre/<genre>")
def get_genre(genre):
    print(genre)
    film = get.get_genre(genre)
    
    return json.dumps(film)



@app.route("/title/<title>")
def get_title(title):
    
    film = get.get_title(title)
    
    return json.dumps(film)



@app.route("/recommender/<title>")
def recommender_system(title):
  titles = rec.get_recommendations(title)
  return json.dumps(titles)

@app.route("/data")
def get_data_visual():
  data = get.get_data_visual()
  return json.dumps(data)








app.run(debug = True)