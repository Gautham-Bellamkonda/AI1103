from random import gauss
import numpy as np
simlen = int(1e7)
a = 4.2483
beta = -0.3
threshold = 0
mu = 0
sigma = 1
s = np.random.normal(mu, sigma, simlen)
ber = np.size(np.nonzero(s > a))
print("The total BER is ", ber)