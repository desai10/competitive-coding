visited = []

def isValidPair(i, j):
    return not (abs(i - j) > 4 or abs(i - j) < 2)

def isValidPerm(arr):
    if len(arr) != len(visited):
        return False

    for i in range(1, len(arr)):
        if not isValidPair(arr[i - 1], arr[i]):
            return False

    return True

def findPerm(cur, cura):
    # print(cur, cura, visited, isValidPerm(cura + [cur]))
    if visited[cur - 1] != -1:
        return []
    visited[cur - 1] = 1
    cura.append(cur)
    if isValidPerm(cura):
        return cura
    if len(cura) >= len(visited):
        return []

    for i in range(cur - 4, cur + 5):
        if i > 0 and i <= len(visited) and isValidPair(i, cur):
            newa = findPerm(i, cura)
            if len(newa) == len(visited):
                return newa

    return []

t = int(input())

while t > 0:

    n = int(input())
    arr = []
    for i in range(1, n + 1):
        visited = [-1] * n
        arr = findPerm(i, [])
        if len(arr) == n:
            break

    if len(arr) == n:
        print(' '.join([str(x) for x in arr]))
    else:
        print(-1)


    t -= 1
