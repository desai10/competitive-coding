y = int(input())
y += 1

while True:
    ma = {}
    sy = str(y)
    dupli = False
    for c in sy:
        if c in ma:
            dupli = True
            break
        ma[c] = 1
    if not dupli:
        print(y)
        break
    y += 1