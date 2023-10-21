import RPi.GPIO as IO
import time
from SettingUp import *

steps = 2000

def draw():
  IO.output(pins["dir_1_digital_pin"],IO.HIGH)
  print(pins["dir_1_digital_pin"], 1)
  for i in range(steps):
    IO.output(pins["step_1_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.output(pins["step_1_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_2_digital_pin"],IO.HIGH)
  print(pins["dir_2_digital_pin"], 1)
  for i in range(steps):
    IO.output(pins["step_2_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.output(pins["step_2_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_1_digital_pin"],IO.LOW)
  print(pins["dir_1_digital_pin"], 0)
  for i in range(steps):
    IO.output(pins["step_1_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.output(pins["step_1_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

  IO.output(pins["dir_2_digital_pin"],IO.LOW)
  print(pins["dir_2_digital_pin"], 0)
  for i in range(steps):
    IO.output(pins["step_2_digital_pin"],IO.HIGH)
    time.sleep(VELOCITY)
    IO.output(pins["step_2_digital_pin"],IO.LOW)
    time.sleep(VELOCITY)

if __name__ == "__main__":
  setUp()
  draw()
  cleanUp()  