t = int(input())

while t > 0:

    n = int(input())
    arr = [int(x) for x in input().split()]

    for i in range(n):
        x = arr[n - 1]
        if i == n - 1:
            x = arr[n - 2]

        for j in range(n - 1):
            if i != j:
                x ^= arr[j]

        if x == arr[i]:
            print(x)
            break

    t -= 1