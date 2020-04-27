n = int(input())

row = input()

ct = 0

for i in range(n - 1):
    if row[i] == row[i + 1]:
        ct += 1

print (ct)