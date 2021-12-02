import os
import pandas
import numpy
import matplotlib.pyplot as plt  # graph drawing library

# x = [] and y = [] it is for Task 1
# x, y = [1, 2, 3, 8], [1, 4, 9, 16]

# Task 1
# plt.plot(x, y, marker='o')
# plt.axis([0, 10, 0, 20])  # set the range of X and Y axes
# plt.xlabel('OX')  # sign the x-axis
# plt.ylabel('OY')  # sign the x-axis
# plt.show()

# plt.plot(x, y, marker='x')
# plt.axis([0, 9, 0, 20])  # set the range of X and Y axes
# plt.xlabel('x - Temperatura')  # sign the x-axis
# plt.ylabel('y - Wiatr')  # sign the x-axis
# plt.show()

# Task 2
# def f(x):
#     return x ** 2 - 5 * x + 6
#
#
# xArr = numpy.linspace(1.0, 4.0, 90, endpoint=True)  # xArr = [1.0, 4.0] - 90 dots
# plt.plot(xArr, f(xArr))  # graph - parabola
# plt.plot(xArr, 0 * xArr, color='pink')  # one more graph - line
# plt.plot([2, 3], [0, 0], 'o', color='green')  # one more 'graph' - 2 green dots
# plt.plot(2.5, -0.25, 'x', color='blue')  # min of function
# plt.show()

# Task 3
# mu, sigma = 100, 20
# xArr = mu + sigma * numpy.random.randn(10000)  # for random samples from
# plt.xlabel('Przedziały')
# plt.ylabel('Prawdopodobienstwo')
# plt.title(r'${Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
# plt.hist(xArr, 50, density=True)  # the histogram of the data
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# mu, sigma = 100, 20
# xArr = mu + sigma * numpy.random.randn(10000)  # for random samples from
# plt.xlabel('Przedziały')
# plt.ylabel('Prawdopodobienstwo')
# plt.title(r'${Histogram\ of\ IQ:}\ \mu=100,\ \sigma=20$')
# plt.hist(xArr, 50, density=True, color='green')  # the histogram of the data
# plt.axis([40, 160, 0, 0.025])
# plt.grid(True)
# plt.show()

# Task 4
labels = ['Tulipany', 'Róże', 'Lilie', 'Żonkile']
sizes = [25, 20, 40, 15]  # percentages of parts
explode = (0, 0.1, 0, 0)  # extend the specified part (explode - wysunięcie wykresu)
fig, ax = plt.subplots()  # without arguments returns a Figure and a single Axes.
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
