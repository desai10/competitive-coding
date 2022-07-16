t = int(input())

while t > 0:

    n = int(input())
    arr = [int(x) for x in input().split()]
    
    st = n - 1
    ans = 0

    for i in range(n - 2, -1, -1):
        ans += arr[i]
        if arr[i] > 0:
            st = i

    while st < n - 1:

        if arr[st] == 0:
            ans += 1

        st += 1

    print(ans)

    t -= 1
