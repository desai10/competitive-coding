t = int(input())

while t > 0:

    n, k = [int(x) for x in input().split()]

    cur = 0

    if n % 2 != 0 and k % 2 == 0:
        print('NO')
    else:
        min = -1
        if n % 2 == 0:
            if (n - (k - 1)) % 2 == 0:
                min = 2
            else:
                min = 1
        else:
            min = 1

        ans = [min for _ in range(k - 1)]
        cur = min * (k - 1)

        if cur >= n:
            print('NO')
        else:
            if (n - cur) % 2 != min % 2:
                print('NO')
            else:
                print('YES')
                ans.append(n - cur)
                print(' '.join([str(x) for x in ans]))

    t -= 1
