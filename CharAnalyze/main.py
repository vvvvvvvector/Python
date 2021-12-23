import collections
import matplotlib.pyplot as plt

str = input("Input text please: ")
str = str.lower()

charDict = {}

for i in str:
    if str.count(i) != 0:
        if i != ' ':
            charDict[i] = int(str.count(i))
    str = str.replace(i, "")

charDict = dict(sorted(charDict.items(), key=lambda item: item[1]))

plt.bar(range(len(charDict)), list(charDict.values()), align='center')
plt.xticks(range(len(charDict)), list(charDict.keys()))

plt.show()
