m_1 = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
m_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_3 = [[1, 2, 3], [4, 5, 6]]


def transpozycja(m):
    row = len(m)
    col = len(m[0])
    new_m = [[0 for x in range(row)] for y in range(col)]
    for i in range(row):
        for j in range(col):
            new_m[j][i] = m[i][j]
    return new_m


new_m = transpozycja(m_1)

for i in range(len(new_m)):
    for j in range(len(new_m[0])):
        print(new_m[i][j], end=' ')
    print()
