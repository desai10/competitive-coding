t = int(input())

while  t > 0:

    a, b, c = [int(x) for x in input().split()]

    s = ''

    if b == 0:
        cc = '1'
        ccc = c + 1
        if a != 0:
            cc = '0'
            ccc = a + 1
        print(cc * ccc)
    else:
        if (b + 1) % 2 == 0:
            s += ('1' * c)
            aa = 1
            for _ in range(b + 1):
                s += str(aa)
                aa = 1 - aa
            s += ('0' * a)
        else:
            s += ('1' * c)
            aa = 1
            for _ in range(b):
                s += str(aa)
                aa = 1 - aa
            s += ('0' * a)
            s += '1'
        print(s)

    t -=  1
