n, f = [int(x) for x in input().split()]

arr = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

k = int(input())

ans = []

while True:
    mxct = -1
    dr = '?'
    r = -1

    for i in range(n):
        ct = 0
        acc = 0
        for j in range(n):
            if acc + arr[i][j] <= f:
                ct += 1
                acc += arr[i][j]
            else:
                break

        if ct > mxct and acc != 0:
            mxct = ct
            dr = 'L'
            r = i + 1

    for i in range(n):
        ct = 0
        acc = 0
        for j in range(n):
            if acc + arr[j][i] <= f:
                ct += 1
                acc += arr[j][i]
            else:
                break

        if ct > mxct and acc != 0:
            mxct = ct
            dr = 'U'
            r = i + 1

    if mxct == -1:
        break

    acc = 0
    for j in range(n):
        aa = -1
        bb = -1
        if dr == 'L':
            aa = r - 1
            bb = j
        elif dr == 'U':
            aa = j
            bb = r - 1
        if acc + arr[aa][bb] <= f:
            acc += arr[aa][bb]
            arr[aa][bb] = 0
        else:
            break

    ans.append((dr, r))
    # for row in arr:
    #     print(row)

    # print()

print(len(ans))
for (dr, r) in ans:
    print(dr, r)
