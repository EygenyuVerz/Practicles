import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# Task-1
# x = [1, 10, 1000]
# for i in x:
#     y = np.log((np.e * (1 / (np.sin(i) + 1))) / (5 / 4 + 1 / (i ** 15))) / np.log(1 + i ** 2)
#     print(y)

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x)')
plt.grid(True)
plt.show()
