import heapq

t = int(input())

while t > 0:

    n = int(input())

    arr = [0 for _ in range(n)]
    q = [(-1 * n, 0, n - 1)]
    heapq.heapify(q)

    ct = 1

    while len(q) > 0:
        cur = heapq.heappop(q)
        l = cur[1]
        r = cur[2]
        if l > r:
            continue
        mid = (l + r) // 2
        arr[mid] = ct
        ct += 1
        if mid - 1 >= 0 and mid - 1 >= l:
            heapq.heappush(q, (-1 * ((mid - 1) - l + 1), l, mid - 1))
        if mid + 1 < n and r >= mid + 1:
            heapq.heappush(q, (-1 * (r - (mid + 1) + 1), mid + 1, r))

    print(' '.join([str(x) for x in arr]))

    t -= 1
