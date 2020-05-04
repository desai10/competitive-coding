t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]
    arrS = set(arr)

    if len(arrS) > k:
        print (-1)
    else:
        req = list(arrS)
        the = -1
        for i in range(1, n + 1):
            if i not in req:
                the = i
                break
        for _ in range(len(req), k):
            req.append(the)
        req.sort()
        newArr = req * n

        print(len(newArr))
        print(' '.join([str(x) for x in newArr]))


