n = int(input())

l = 0
r = 0

for _ in range(n):
    li, ri = [int(x) for x in input().split()]
    l += li
    r += ri

print (min(l, n - l) + min(r, n - r))
