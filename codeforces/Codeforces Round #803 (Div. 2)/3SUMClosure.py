t = int(input())

while t > 0:

    n = int(input())
    arr = [int(x) for x in input().split()]
    
    ctn = 0
    ctp = 0
    ctz = 0

    na = []

    for x in arr:
        if x > 0:
            ctp += 1
            na.append(x)
        elif x < 0:
            ctn += 1
            na.append(x)
        else:
            ctz += 1

    if ctp > 2 or ctn > 2:
        print("NO")
    else:
        if ctz >= 2:
            na.append(0)
        if ctz >= 1:
            na.append(0)

        if len(na) < 3:
            print("YES")
        else:
            possi = True
            ma = {}
            for x in na:
                ma[x] = 1
            for i in range(len(na)):
                for j in range(len(na)):
                    for k in range(len(na)):
                        if i != k and j != k and i != j:
                            if (na[i] + na[j] + na[k]) not in ma:
                                possi = False
                                break
                        if not possi:
                            break
                    if not possi:
                        break
                if not possi:
                    break

            if possi:
                print("YES")
            else:
                print("NO")
                
    t -= 1
