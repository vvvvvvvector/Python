import math

def distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += math.pow((x[i] - y[i]), 2)
    return math.sqrt(sum)

x = [1, 2, 3]
y = [2, 4, -1]

print(distance(x, y))
