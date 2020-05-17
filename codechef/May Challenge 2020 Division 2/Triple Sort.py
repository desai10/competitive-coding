t = int(input())

while t > 0:

    n, ok = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    pos = {}

    for (i, x) in enumerate(arr, 1):
        pos[x] = i

    ops = []
    oldArr = arr[:]

    # print(arr)

    for i in range(1, n + 1):
        if arr[i - 1] != i:
            j = pos[i]
            k = arr[i - 1]

            if j != k:
                aa = arr[i - 1]
                arr[i - 1] = arr[j - 1]
                pos[arr[j - 1]] = i
                arr[j - 1] = arr[k - 1]
                pos[arr[k - 1]] = j
                arr[k - 1] = aa
                pos[aa] = k

                if k > j:
                    ops.append((k, j, i))
                else:
                    ops.append((i, k, j))

    for i in range(1, n + 1):
        if arr[i - 1] != i:
            j = pos[i]
            k = arr[i - 1]

            if j == k:

                for kk in range(i + 1, n + 1):
                    if kk != j and arr[kk - 1] != kk:
                        k = kk
                        break

                if k == j:
                    break

            aa = arr[i - 1]
            arr[i - 1] = arr[j - 1]
            pos[arr[j - 1]] = i
            arr[j - 1] = arr[k - 1]
            pos[arr[k - 1]] = j
            arr[k - 1] = aa
            pos[aa] = k

            if k > j:
                ops.append((k, j, i))
            else:
                ops.append((i, k, j))

            # print(i, j, k, arr)

    isdone = True
    for (i, x) in enumerate(arr, 1):
        if i != x:
            isdone = False
            break

    if len(ops) > ok or not isdone:
        print(-1)
    else:
        print(len(ops))
        for ele in ops:
            print(ele[0], ele[1], ele[2])

    t -= 1
