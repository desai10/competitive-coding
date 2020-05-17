al = {}
visited = {}


def minSwaps(arr):
    n = len(arr)

    arrpos = [(i, x) for (i, x) in enumerate(arr)]

    arrpos.sort(key=lambda it: it[1])

    vis = {k: False for k in range(n)}

    ans = 0
    # print(arr, arrpos, al)
    for i in range(1, n):

        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 1
        vis[i] = True
        j = arrpos[i][0]
        pre = i
        while not vis[j]:
            vis[j] = True
            # print(pre, j, cycle_size)
            visited = {}
            if not hasPath(pre, j, {}):
                cycle_size += 1

            pre = j
            j = arrpos[j][0]

        if hasPath(j, pre, {}):
            cycle_size -= 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


def hasPath(src, dest, viz):
    # print('(', src, dest, ')', end=' ')
    if src == dest:
        return True
    if src in viz:
        return False
    # print('yay', end=' ')

    viz[src] = 1

    path = False
    if src not in al:
        al[src] = []
    for p in al[src]:
        path = path or hasPath(p, dest, viz)
        if path:
            return path

    return path


t = int(input())

while t > 0:

    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    al = {}
    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        if x not in al:
            al[x] = []
        if y not in al:
            al[y] = []
        al[x].append(y)
        al[y].append(x)

    narr = [0 for _ in range(len(arr) + 1)]

    for (i, x) in enumerate(arr, 1):
        narr[x] = i

    # ct = 0

    # for i in range(1, n + 1):
    #     if narr[i] != i:
    #         visited = {}
    #         if hasPath(i, arr[i - 1]):
    #             aa = narr[i]
    #             narr[i] = narr[arr[i - 1]]
    #             narr[arr[i - 1]] = aa

    print(minSwaps(narr))

    t -= 1
