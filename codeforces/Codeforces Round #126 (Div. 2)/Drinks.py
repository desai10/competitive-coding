n = int(input())

p = [int(x) for x in input().split()]

psum = sum(p)

print ((psum  / (n * 100)) * 100)