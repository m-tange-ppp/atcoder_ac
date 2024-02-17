#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

X, Y, Z = mi()
S = si()

l = len(S)
dp = [[inf, inf] for _ in range(l)]
for i in range(l):
    if i == 0:
        if S[i] == "a":
            dp[i][0] = min(X + Z, Y + Z)
            dp[i][1] = min(X, Y + 2 * Z)
        else:
            dp[i][0] = min(X + Z, Y + Z)
            dp[i][1] = min(Y, X + Z * 2)
    else:
        if S[i] == "a":
            dp[i][0] = min(dp[i - 1][0] + X + 2 * Z, dp[i - 1][0] + Y, dp[i - 1][1] + X + Z, dp[i - 1][1] + Y + Z)
            dp[i][1] = min(dp[i - 1][1] + Y + 2 * Z, dp[i - 1][1] + X, dp[i - 1][0] + X + Z, dp[i - 1][0] + Y + Z)
        else:
            dp[i][0] = min(dp[i - 1][0] + Y + 2 * Z, dp[i - 1][0] + X, dp[i - 1][1] + X + Z, dp[i - 1][1] + Y + Z)
            dp[i][1] = min(dp[i - 1][1] + X + 2 * Z, dp[i - 1][1] + Y, dp[i - 1][0] + X + Z, dp[i - 1][0] + Y + Z)
print(min(dp[-1][0], dp[-1][1]))