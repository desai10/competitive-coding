n = int(input())

arr = []

if n % 2 != 0:
    print ('-1')
else:
    for i in range(1, n + 1, 2):
        arr.append(i + 1)
        arr.append(i)

    print (' '.join(list(map(lambda x: str(x), arr))))
