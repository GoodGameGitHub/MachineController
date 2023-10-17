from Server import app
from flask import render_template
import subprocess as sp
import os

@app.route('/drawing/<string:shape>',methods=['GET'])
def drawingController(shape):

    return render_template("Draw.html",shape=shape)
