from Server import app
from flask import render_template
import os

@app.route('/',methods=['GET'])
def indexControllerGetPage():
    return render_template("Index.html")


@app.route('/',methods=['POST'])
def indexControllerPostImage():
    return render_template("Draw.html")
