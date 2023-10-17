import RPi.GPIO as IO

pins = {"servo_pwm_pin": 17, 
        "dir_1_digital_pin": 18, 
        "step_1_digital_pin": 19, 
        "dir_2_digital_pin": 20, 
        "step_2_digital_pin": 21 
      }

def setUp():
    IO.setmode(IO.BCM)
    for i in pins.values():
        IO.setup(i,IO.OUT)

def cleanUp():
    IO.cleanup()