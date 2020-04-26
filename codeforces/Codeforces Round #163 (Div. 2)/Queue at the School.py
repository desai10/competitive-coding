nt = input().split()
n = int(nt[0])
t = int(nt[1])
line = input()

lineList = [x for x in line]

for tt in range(t):
    hasSwapped = False
    for i in range(n - 1):
        if lineList[i] == 'B' and lineList[i + 1] == 'G' and not hasSwapped:
            lineList[i] = 'G'
            lineList[i + 1] = 'B'
            i += 1
            hasSwapped = True
        else:
            hasSwapped = False

print (''.join(lineList))