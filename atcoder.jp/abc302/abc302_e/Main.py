#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

N, Q = mi()
g = [set() for _ in range(N + 1)]
linked = defaultdict(int)
nsum = 0
for _ in range(Q):
    q = li()
    if q[0] == 1:
        u, v = q[1], q[2]
        g[u].add(v)
        g[v].add(u)
        if linked[u] == 0:
            nsum += 1
        if linked[v] == 0:
            nsum += 1
        linked[u] += 1
        linked[v] += 1
    else:
        v = q[1]
        for n in g[v]:
            g[n].remove(v)
            linked[n] -= 1
            if linked[n] == 0:
                nsum -= 1
        g[v] = set()
        if linked[v] > 0:
            nsum -= 1
        linked[v] = 0
    print(N - nsum)