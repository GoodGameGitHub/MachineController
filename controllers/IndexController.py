from Server import app
from flask import render_template, redirect
import os


@app.route('/',methods=['GET'])
def indexControllerGetPage():
    if app.config["DMP_MW"] == "0":
        return render_template("Index.html")
    else:
        shape = app.config["SHAPE"]
        return redirect(f"/drawing/{shape}")


@app.route('/',methods=['POST'])
def indexControllerPostImage():
    return render_template("Draw.html")
