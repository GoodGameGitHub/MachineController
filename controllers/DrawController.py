from Server import app
from flask import render_template, redirect
import subprocess as sp
import os

@app.route('/drawing/<string:shape>',methods=['GET'])
def drawingController(shape):
    if app.config["DMP_MW"] == "0":
        command = "ifconfig wlan0 | awk '/inet / {print $2}'"
        result = sp.run(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True)
        if result.returncode != 0:
            print("Command failed")
            print("Error:")
            print(result.stderr)
            return "error"
        
        if processExists():
            mappingFiles = {"square":"DrawingSquareScript.py",
                            "triangle":"DrawingTriangleScript.py",
                            "rectangle":"DrawingRectangleScript.py"}
            fileName = f"{app.config['SCRIPTS_PATH']}{mappingFiles[shape]}"
            process = sp.Popen(["python3",fileName], stdout = sp.PIPE, stderr = sp.PIPE)
            app.config["SUBPROCESS_ID"] = process.pid
            process = None

        app.config["SHAPE"] = shape
        app.config["DMP_MW"] = "1"
        data = {"ip":result.stdout[:-1],"shape":shape}
        return render_template("Draw.html",data=data)
    else:
        shape = app.config["SHAPE"]
        return redirect(f"/drawing/{shape}")
    


def processExists():
    return False if (app.config["SUBPROCESS_ID"] == "null") else True 


     
