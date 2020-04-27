from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

inp = ''
# dp = []

@lru_cache(maxsize=10000)
def calculatePossibilities(s, index):

    if index >= len(s):
        return 1

    if s[index] == '0':
        return 0

    # if dp[index] != -1:
    #     return dp[index]

    tAns = calculatePossibilities(s, index + 1)

    if (index + 1 < len(s) and int(s[index:index + 2]) <= 26):
        tAns += calculatePossibilities(s, index + 2)

    # dp[index] = tAns
    return tAns


inp = input()
while inp != '0':

    # dp = [-1 for _ in range(5005)]
    if (inp != ''):
        print (calculatePossibilities(inp, 0))

    inp = input()
