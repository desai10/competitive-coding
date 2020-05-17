arr = [7, 6, 5, 4, 3, 2, 1]
ma = {}
q = []
q.append((arr, [arr], []))
while len(q) > 0:
    curq = q.pop(0)
    cs = curq[0]
    css = sorted(curq[0])
    if css == cs:
        print('done')
        for ee in curq[1]:
            print(ee)
        print('aaaaa')
        for ee in curq[2]:
            print(ee)
        break
    for i in range(len(curq[0])):
        for j in range(i + 1, len(curq[0])):
            for k in range(j + 1, len(curq[0])):
                newq = curq[0][:]
                ops = curq[2][:]
                steps = curq[1][:]
                ops.append((i, j, k))
                newq[i] = curq[0][j]
                newq[j] = curq[0][k]
                newq[k] = curq[0][i]
                steps.append(newq)
                if tuple(newq) not in ma:
                    q.append((newq, steps, ops))
                    ma[tuple(newq)] = 1
                newq = curq[0][:]
                ops = curq[2][:]
                steps = curq[1][:]
                ops.append((i, j, k))
                newq[i] = curq[0][k]
                newq[j] = curq[0][i]
                newq[k] = curq[0][j]
                steps.append(newq)
                if tuple(newq) not in ma:
                    q.append((newq, steps, ops))
                    ma[tuple(newq)] = 1
print('asdasdas')
