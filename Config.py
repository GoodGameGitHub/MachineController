import os


DEBUG = True
UPLOAD_FOLDER = './static/picture_loading/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}
MACHINE_STATUS= "STALE"
SHAPE = ""
SUBPROCESS_ID = "null"
SCRIPTS_PATH = "/home/kevin/Desktop/drawingMachine/app/scripts"

TESTING_PIN_NAME = "null"
TESTING_PIN_VALUE = "null"
TESTING_PIN_BCM = "null"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)