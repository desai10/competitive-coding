from collections import deque

t = int(input())

while t > 0:

    [n, q] = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    l = 0
    r = n - 1
    ans = [0 for _ in range(n)]

    while l <= r:
        m = (l + r) // 2

        tans = [0 for _ in range(n)]
        qq = q
        for i in range(n):
            if i < m:
                if arr[i] <= qq:
                    tans[i] = 1
            else:
                tans[i] = 1
                if qq == 0:
                    qq = -1
                    break
                if arr[i] > qq:
                    qq -= 1

        if qq >= 0:
            r = m - 1
            ans = [x for x in tans]
        else:
            l = m + 1

    print(''.join(map(str, ans)))

    t -= 1
