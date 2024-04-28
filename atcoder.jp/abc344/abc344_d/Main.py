#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
INF=float('inf'); MOD=998244353 #10**9+7

T = si()
N = ii()
S = list()
for _ in range(N):
    AS = list(sys.stdin.readline().rstrip().split())
    S.append(AS[1:])

L = len(T)
dp = [[INF for _ in range(L + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(L + 1):
        if dp[i + 1][j] > dp[i][j]: # i = Lのときにこの処理をするのを忘れてた
            dp[i + 1][j] = dp[i][j]
        if j < L:
            for s in S[i]:
                if len(s) + j <= L and T[j:len(s) + j] == s:
                    if j == 0:
                        dp[i + 1][j + len(s)] = 1
                    elif dp[i + 1][j + len(s)] > dp[i][j] + 1:
                        dp[i + 1][j + len(s)] = dp[i][j] + 1
# print(dp)
print(dp[-1][-1] if dp[-1][-1] < INF else -1)