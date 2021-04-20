import numpy as np
import matplotlib.pyplot as plt
import math
simlen = int(1e5)
s = np.random.uniform(-1,1,simlen)
y = []
for i in range (0, simlen):
    y.append((s[i] + 1)*(s[i] + 1))

count, bins, ignored = plt.hist(y, 25, density=True)

x = np.arange(0.04, 4.0, 0.00001)
def func(x):
    return 0.25/math.sqrt(x)

vec_f = np.vectorize(func)
plt.plot(x, vec_f(x))
plt.xlabel("$y$")
plt.ylabel("$Pr(Y=y)$")
plt.legend(["Theoretical", "Simulated"])
plt.show()