t =  int(input())

while t > 0:

    tt = input()
    ca = sorted(tt)
    if (ca[0] == ca[len(ca) - 1 ]):
        print (tt)
    else:
        newTt = "" + tt[0]
        pre = tt[0]
        i = 1
        while i < len(tt):
            if pre == tt[i]:
                pre = '0' if pre == '1' else '1'
            else:
                pre = tt[i]
                i += 1
            newTt += pre

        print(newTt)

    t -= 1