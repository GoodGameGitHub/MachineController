from Server import app
import subprocess as sp
import os


@app.route('/processing',methods=['GET'])
def drawing():
    dp_exists = False
    return "currently drawing" if dp_exists else "not drawing"
    
