from Server import app
import subprocess as sp
import os


@app.route('/processing',methods=['GET'])
def drawing():
    dp_exists = True
    return "currently_drawing" if dp_exists else "not_drawing"
    
