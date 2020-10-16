import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

N = 500
t = np.linspace(0,12,num=N)
# w = pi
fs = 0.5
x1 =  np.cos(2 * math.pi * fs * t)
plt.subplot(111)
plt.plot(t,x1)
plt.ylim(-2.0,2.0)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
