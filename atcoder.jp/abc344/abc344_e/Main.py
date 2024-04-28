#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
from collections import defaultdict, deque
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
A = [0] + li() + [-1]
Q = ii()
next = defaultdict(int)
prev = defaultdict(int)
for i in range(N + 1):
    next[A[i]] =A[i + 1]
    prev[A[i + 1]] =A[i]

for _ in range(Q):
    q = li()
    if q[0] == 1:
        x, y = q[1], q[2]
        prev[next[x]] = y
        next[y] = next[x]
        next[x] = y
        prev[y] = x

    else:
        x = q[1]
        n = next[x]
        p = prev[x]
        next[p] = n
        prev[n] = p
ans = []
now = next[0]
while now != -1:
    ans.append(now)
    now = next[now]
print(*ans)