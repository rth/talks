import numpy as np
from time import sleep

X = np.ones((3000, 3000))

while True:
    X.dot(X)
    sleep(1)
    s = 0
    for i in range(1000):
        s += i
