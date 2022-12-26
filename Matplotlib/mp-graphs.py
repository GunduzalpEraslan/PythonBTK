import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y,"o--r")
# plt.axis([0,6,0,20])

# plt.title("Grafik Başlığı")
# plt.xlabel("x- label")
# plt.ylabel("y-label")

# plt.show()
'''
x = np.linspace(0,2,100)

plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()

plt.title("Simple Plot")
plt.show()
'''


x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2)

axs[0,0].plot(x,x, color = "red")
axs[0,1].plot(x,x**2, color = "bule")
axs[1,0].plot(x,x**3, color = "green")
axs[1,1].plot(x,x**4, color = "yellow")

plt.show()
'''
fig,axs = plt.subplots(3)

axs[0].plot(x,x, color = "red")
axs[0].set_title("Linear")

axs[1].plot(x,x**2, color = "green")
axs[1].set_title("Quadratic")

axs[2].plot(x,x**3, color = "yellow")
axs[2].set_title("Cubic")

plt.tight_layout()
plt.show()

'''


import pandas as pd

df = pd.read_csv("")