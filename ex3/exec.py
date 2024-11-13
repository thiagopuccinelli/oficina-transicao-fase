import numpy as np 
import os 


temps = [0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.05,1.1]

os.system("lmp -in run2.lmp -v told 0.5 -v t 0.5 ")
for i in range(1,len(temps)+1):
    os.system("lmp -in run2.lmp -v told {} -v t {} ".format(temps[i-1],temps[i]))
