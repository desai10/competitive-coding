n = int(input())

lst = [int(x) for x in input().split()]

ct = 0
mi = lst[0]
mx = lst[0]

for x in lst[1:]:
    if x > mx or x < mi:
        ct += 1
    if x > mx:
        mx = x
    if x < mi:
        mi = x

print (ct)