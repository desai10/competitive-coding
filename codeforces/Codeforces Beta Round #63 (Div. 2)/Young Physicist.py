n = int(input())
tx = 0
ty = 0
tz = 0

for i in range(n):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    tx += x
    ty += y
    tz += z

if tx == 0 and ty == 0 and tz == 0:
    print ('YES')
else:
    print ('NO')
