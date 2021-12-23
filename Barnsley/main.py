import matplotlib.pyplot as plt  # graph drawing library
from matplotlib.pyplot import figure

from random import randint

x, y, n = [0], [0], 0

for i in range(0, 100001):
    randNum = randint(1, 100)

    if randNum == 1:  # f1
        x.append(0)  # = x[n + 1]
        y.append(0.16 * y[n])  # = y[n + 1]

    if randNum >= 2 and randNum < 87:  # f2
        x.append(0.85 * x[n] + 0.04 * y[n])
        y.append(-0.04 * x[n] + 0.85 * y[n] + 1.6)

    if randNum >= 87 and randNum < 94:  # f3
        x.append(0.2 * x[n] - 0.26 * y[n])
        y.append(0.23 * x[n] + 0.22 * y[n] + 1.6)

    if randNum >= 94 and randNum < 101:  # f4
        x.append(-0.15 * x[n] + 0.28 * y[n])
        y.append(0.26 * x[n] + 0.24 * y[n] + 0.44)

    n += 1


figure(figsize=(8, 6), dpi=100)
plt.scatter(x, y, s=0.5,  c='#D645F7')
plt.axis('off')

plt.show()
