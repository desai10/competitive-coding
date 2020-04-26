def isGood(x, y):
    if x >= 0 and x < 3 and y >= 0 and y < 3:
        return True
    return False

lg = [[0, 0, 0] for _ in range(3)]

g = [[1, 1, 1] for _ in range(3)]

for i in range(3):
    l = input().split()
    for (ii, li) in enumerate(l):
        lg[i][ii] = int(li) % 2

for (i, row) in enumerate(lg):
    for (j, cell) in enumerate(row):
        if lg[i][j] == 1:
            g[i][j] = 1 - g[i][j]
            if isGood(i -1, j):
                g[i-1][j] = 1 - g[i-1][j]
            if isGood(i, j -1):
                g[i][j-1] = 1 - g[i][j-1]
            if isGood(i + 1, j):
                g[i+1][j] = 1 - g[i+1][j]
            if isGood(i, j + 1):
                g[i][j+1] = 1 - g[i][j+1]

for row in g:
    print (''.join(list(map(lambda x: str(x), row))))
