n = int(input())

arr = list(map(int, input().split()))

mx = max(arr)
mi = min(arr)

mip = -1
mxp = -1

for (i, x) in enumerate(arr, 1):
    if x == mx and mxp == -1:
        mxp = i
    if x == mi:
        mip = i
        if mxp == -1:
            mip += 1

print ((n - mip) + (mxp - 1))

