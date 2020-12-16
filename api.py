from flask import Flask, request, render_template

from flask import Flask, request
from flask import request
import markdown.extensions.fenced_code

import  src.getdata as get
import src.recommender  as rec

import json

app = Flask(__name__)

@app.route("/")
def index():
  
   
  readme_file = open("index.md","r")
  md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
  return md_template_string


@app.route("/genre/<genre>")
def get_genre(genre):
    # print(genre)
    # film = get.get_genre(genre)
    
    # return json.dumps(film)
    film = [{'title': 'Ek', 'rating': 9.8, 'trailer': 'https://www.imdb.com/video/vi712424985?playlistId=tt12492650&ref_=tt_ov_vi'}, {'title': 'Il cavaliere oscuro', 'rating': 9.0, 'trailer': 'https://www.imdb.com/video/vi324468761?playlistId=tt0468569&ref_=tt_ov_vi'}, {'title': 'Ramayana: The Legend of Prince Rama', 'rating': 9.0, 'trailer': None}]
    return render_template('podium.html', data = film)



@app.route("/title/<title>")
def get_title(title):
    
    film = get.get_title(title)
    
    return json.dumps(film)



@app.route("/recommender/<title>")
def recommender_system(title):
  titles = rec.get_recommendations(title)
  return json.dumps(titles)










app.run(debug = True)