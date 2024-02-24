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

Q = ii()
que = deque()
que.append(1)
res = 1
for _ in range(Q):
    q = li()
    t = q[0]
    if t == 1:
        x = q[1]
        que.append(x)
        res = (res * 10 + x) % MOD
    elif t == 2:
        x = que.popleft()
        res -= x * pow(10, len(que), MOD)
        res %= MOD
    else:
        print(res)