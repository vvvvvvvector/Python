# The game of life

from random import randint
from copy import deepcopy
import time
import os

N = int(input("Input N: "))

current = [[randint(0, 1) for x in range(N + 1)] for y in range(N + 1)]
next = [[0 for x in range(N + 1)] for y in range(N + 1)]

def check_cell(current, row, col):
    count = 0
    for y in range(col - 1, col + 2):
        for x in range(row - 1, row + 2):
            if current[y][x]:
                count += 1

    if current[col][row]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    for x in range(1, N - 1):
        for y in range(1, N - 1):
            if current[y][x]:
                print('*', end=' ')
            else:
                print(' ', end=' ')
            next[y][x] = check_cell(current, x, y)
        print()

    time.sleep(1 / 7.0)
    os.system('cls')  # os.system('clear') for linux; os.system('cls') for windows
    current = deepcopy(next)
