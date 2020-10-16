"""
    指数信号
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1.0,1.0,1000)  #通过linspace函数指定t的取值范围
plt.ylim(0,5)                          #定义纵轴取值范围
plt.subplot(221)     #显示的位置  
ft = np.exp(-t)              #调用exp函数计算指数信号
plt.plot(t,ft)                #绘图
plt.subplot(221)
ft1 = np.exp(t)
plt.plot(t,ft1)
plt.subplot(221)
ft2 = np.exp(0*t)
plt.plot(t,ft2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

