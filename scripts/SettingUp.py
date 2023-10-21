import RPi.GPIO as IO

pins = {"servo_pwm_pin": 33, 
        "dir_1_digital_pin": 16, 
        "step_1_digital_pin": 18, 
        "dir_2_digital_pin": 13, 
        "step_2_digital_pin": 15 
      }

VELOCITY = 0.001

def setUp():
    IO.setmode(IO.BCM)
    for i in pins.values():
        print(i)
        IO.setup(i,IO.OUT)

def cleanUp():
    IO.cleanup()
