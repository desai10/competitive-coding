t = int(input())

while t > 0:
    x, y = [int(q) for q in input().split( )]
    a, b = [int(q) for q in input().split()]
    if 2 * a <= b:
        print ((abs(x) + abs(y)) * a)
    else:
        tot = 0
        if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
            tot += min(abs(x), abs(y)) * b
            tot += (abs(x) - min(abs(x), abs(y))) * a
            tot += (abs(y) - min(abs(x), abs(y))) * a
        else:
            tot += abs(x) * a
            tot += abs(y) * a
        print(tot)
    t -= 1
