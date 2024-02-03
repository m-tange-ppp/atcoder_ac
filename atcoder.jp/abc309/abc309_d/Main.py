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

N1, N2, M = mi()
G = [[] for _ in range(N1 + N2)]
for _ in range(M):
    a, b = mi(1)
    G[a].append(b)
    G[b].append(a)
d1 = [-1] * N1
d2 = [-1] * N2
que1 = deque()
que1.append(0)
d1[0] = 0
que2 = deque()
que2.append(N1 + N2 - 1)
d2[N2 - 1] = 0
while que1:
    now = que1.popleft()
    for n in G[now]:
        if d1[n] == -1:
            d1[n] = d1[now] + 1
            que1.append(n)
while que2:
    now = que2.popleft()
    for n in G[now]:
        if d2[n - N1] == -1:
            d2[n - N1] = d2[now - N1] + 1
            que2.append(n)
print(max(d1) + max(d2) + 1)
