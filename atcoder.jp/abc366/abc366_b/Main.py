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

N = ii()
S = [si() for _ in range(N)]

max_s_l = 0
for s in S:
    max_s_l = max(max_s_l, len(s))

T = [[""] * N for _ in range(max_s_l)]
for i in range(max_s_l):
    isExist = False
    for j in range(N):
        if len(S[j]) > i:
            T[i][N - 1 - j] = S[j][i]
            isExist = True
        else:
            if isExist:
                T[i][N - 1 - j] = "*"

for t in T:
    print("".join(t))
