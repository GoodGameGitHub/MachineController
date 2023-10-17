import RPi.GPIO as IO
from SettingUp import pins
from Config import VELOCITY
import time
from SettingUp import *

steps = 400

def draw():
  IO.output(pins["dir_1_digital_pin"],IO.HIGH)
  for i in range(steps):
    IO.output(pins["step_1_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.outpunt(pins["step_1_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_2_digital_pin"],IO.HIGH)
  for i in range(steps):
    IO.output(pins["step_2_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.outpunt(pins["step_2_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_1_digital_pin"],IO.LOW)
  for i in range(steps):
    IO.output(pins["step_1_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.outpunt(pins["step_1_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_2_digital_pin"],IO.LOW)
  for i in range(steps):
    IO.output(pins["step_2_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.outpunt(pins["step_2_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

if __name__ == "__main__":
  setUp()
  draw()
  cleanUp()