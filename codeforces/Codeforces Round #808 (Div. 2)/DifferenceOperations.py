t = int(input())

while t > 0:

    n = int(input())
    arr = [int(x) for x in input().split()]
    
    ct = 0

    for i in range(1, n):
        if arr[i] % arr[0] == 0:
            ct += 1

    if ct == n - 1:
        print("YES")
    else:
        print("NO")

    t -= 1
