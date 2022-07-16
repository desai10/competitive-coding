t = int(input())

while t > 0:

    [n, l, r] = [int(x) for x in input().split()]
    
    possi = True
    ans = []

    for i in range(1, n + 1):
        md = r % i
        req = r - md
        if req < l:
            possi = False
            break
        ans.append(req)

    if possi:
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

    t -= 1
