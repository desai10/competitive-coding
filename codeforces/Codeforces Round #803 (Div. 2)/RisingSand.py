t = int(input())

while t > 0:

    [n, k] = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    ct = 0

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] + arr[i + 1]:
            ct += 1

    if k == 1:
        ct = n // 2
        if n % 2 == 0:
            ct -= 1

    print (ct)

    t -= 1