s1 = input()
s2 = input()

s = ''

for c1, c2 in list(zip(s1, s2)):
    if c1 == c2:
        s += '0'
    else:
        s += '1'

print (s)