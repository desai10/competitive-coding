t = int(input())

while t > 0:

    [n, q] = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    cur = 0
    ans = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        if arr[i] <= cur:
            ans[i] = 1
        else:
            if cur != q:
                cur += 1
                ans[i] = 1

    print(''.join(map(str, ans)))

    t -= 1
