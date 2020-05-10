t = int(input())

while t > 0:

    ans = []
    n = input()
    div = 0
    sz = len(n)
    for i in range(sz):
        if n[sz - 1 -i] != '0':
            # print(sz - 1 - i, n[sz - 1 - i])
            ans.append(n[sz - 1 - i] + ('0') * div)
        div += 1

    print(len(ans))
    for a in ans:
        print(a, end=' ')
    print()


    t -= 1
