from flask import Flask


app = Flask(__name__)
app.config.from_object('Config')

from controllers.IndexController import *
from controllers.DrawController import *
from models.DrawModel import *
#import scripts.SettingUp 
#from controllers.DrawController import *


if __name__ == '__main__':
	#scripts.SettingUp.cleanUp()
	#scripts.SettingUp.setUp()
	app.run(host='0.0.0.0',port=80)




