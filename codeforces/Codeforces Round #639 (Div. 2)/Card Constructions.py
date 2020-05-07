t = int(input())

# arr = [x * (3 * x + 1) / 2 for x in range()]

def search(l, r, ele):
    if l > r:
        return -1
    mid = (l + r) // 2
    val = mid * ((3 * mid) + 1) // 2
    # print(l, r, mid, val, ele)
    if val == ele:
        return val
    if val > ele:
        return search(l, mid - 1, ele)
    return max(val, search(mid + 1, r, ele))

while t > 0:
    n = int(input())
    ct = 0
    while n > 0:
        maxPy = search(1, 1000000000, n)
        if maxPy > 0:
            n -= maxPy
            ct += 1
        else:
            break

    print(ct)
    t -= 1
