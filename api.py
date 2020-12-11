from flask import Flask, request

from flask import Flask, request
from flask import request
import markdown.extensions.fenced_code

import  src.getdata as get
#import src.posdata  as pos
#import src.sentiment as sen
import json

app = Flask(__name__)

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















app.run(debug = True)