n = int(input())

mxTot = -1
cur = 0

for _ in range(n):
    a, b = [int(x) for x in input().split()]
    cur += b
    cur -= a
    if mxTot < cur:
        mxTot = cur

print(mxTot)
