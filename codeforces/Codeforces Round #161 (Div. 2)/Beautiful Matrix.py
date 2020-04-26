posr = 0
posc = 0

for i in range(1, 6):
    row = input()
    if '1' in row:
        posr = i
        posc = row.split().index('1') + 1
        break

print (abs(3 - posr) + abs(3 - posc))
