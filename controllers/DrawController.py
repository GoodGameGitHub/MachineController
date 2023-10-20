from Server import app
from flask import render_template
import subprocess as sp
import os

@app.route('/drawing/<string:shape>',methods=['GET'])
def drawingController(shape):
    command = "ifconfig wlan0 | awk '/inet / {print $2}'"
    result = sp.run(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True)
    if result.returncode != 0:
        print("Command failed")
        print("Error:")
        print(result.stderr)

    data = {"ip":result.stdout[:-1],"shape":shape}
    return render_template("Draw.html",data=data)
