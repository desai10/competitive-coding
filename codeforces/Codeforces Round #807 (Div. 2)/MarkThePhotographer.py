t = int(input())

while t > 0:

    [n, xx] = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    arr.sort()
    used = {}

    ct = 0

    for i in range(n):
        don = False
        for j in range(i + 1, 2 * n):
            if arr[i] + xx <= arr[j] and j not in used:
                don = True
                used[j] = 1
                break

        if don:
            ct += 1

    if ct != n:
        print("NO")
    else:
        print("YES")

    t -= 1
