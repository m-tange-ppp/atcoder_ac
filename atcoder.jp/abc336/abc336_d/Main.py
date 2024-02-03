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
A = li()
lp = [0] * N
rp = [0] * N
lp[0] = 1
rp[0] = 1
ans = 0
for i in range(1, N):
    lp[i] = min(lp[i - 1] + 1, A[i])
    rp[i] = min(rp[i - 1] + 1, A[N - 1 - i])
rp = rp[::-1]
for i in range(N):
    ans = max(ans, min(lp[i], rp[i]))
print(ans)