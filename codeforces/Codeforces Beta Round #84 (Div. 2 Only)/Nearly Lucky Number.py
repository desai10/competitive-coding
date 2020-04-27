n = input()

ct = 0

for c in n:
    if c in ['4', '7']:
        ct += 1

if ct == 4 or ct ==7:
    print ("YES")
else:
    print("NO")