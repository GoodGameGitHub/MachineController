#!/usr/bin/python3

import time
import os
import subprocess as sp
iterations = 15

for i in range(iterations):
	string = f"iteración: {i}"
	print(string)
	sp.run(f"echo {string} >> output.txt",shell=True)
	time.sleep(2)

print("programa terminado")
