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

N = ii()
ryori = [li() for _ in range(N)]

dp = [0] * (2 * N)

if ryori[0][0] == 0:
    dp[0] = max(dp[0], ryori[0][1])
else:
    dp[1] = max(dp[1], ryori[0][1])

for i in range(1, N):
    if ryori[i][0] == 0:
        dp[2 * i] = max(dp[2 * i - 2], dp[2 * i - 2] + ryori[i][1], dp[2 * i - 1] + ryori[i][1])
        dp[2 * i + 1] = dp[2 * i - 1]
    else:
        dp[2 * i] = dp[2 * i - 2]
        if ryori[i][1] >= 0:
            dp[2 * i + 1] = max(dp[2 * i - 2] + ryori[i][1], dp[2 * i - 1])
        else:
            dp[2 * i + 1] = dp[2 * i - 1]

print(max(dp[2 * N - 2], dp[2 * N - 1]))