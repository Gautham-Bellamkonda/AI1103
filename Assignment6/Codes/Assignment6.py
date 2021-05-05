import numpy as np
import math
import matplotlib.pyplot as plt


theta = 5.0
n = 10
sum_arr = np.zeros(200)
count_arr = np.zeros(200)
res_arr = np.zeros(200)
simlen = int(1e6)
s = np.random.exponential(theta, (simlen, n))
for i in range(simlen):
    x1 = min(s[i])
    t = sum(s[i])
    sum_arr[math.ceil(t)]+= x1
    count_arr[math.ceil(t)]+=1

for i in range(200):
    res_arr[i] = (sum_arr[i])/(count_arr[i])

def func(x):
    return x/(n*n)

vec_func = np.vectorize(func)
x = np.arange(1, 100, 1)

plt.plot(x, vec_func(x))
plt.plot(x, res_arr[x])
plt.xlabel("$t$")
plt.ylabel("$E(X_{(1)}|T=t)$")
plt.legend(["Theoretical", "Simulated"])
plt.grid()
plt.show()