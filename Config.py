import os

VELOCITY = 0.001
DEBUG = True
UPLOAD_FOLDER = './static/picture_loading/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)