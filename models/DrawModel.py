from Server import app
import subprocess as sp
import os


@app.route('/processing',methods=['GET'])
def drawing():
    #if app.config["MACHINE_STAUS"] = 
    


@app.route('/changeState',methods=['GET'])
def switchingState():
    app.config["DMP_MW"] = "0" if app.config["DMP_MW"] == "1" else "1"
    return f"changed state to {app.config['DMP_MW']}"