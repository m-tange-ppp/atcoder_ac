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

N = ii()
A = li(1)
ans = []
G = [[] for _ in range(N)]
q = deque()
for i, a in enumerate(A):
    if a != -2:
        G[a].append(i)
    else:
        q.append(i)
        ans.append(i)
while q:
    now = q.pop()
    for n in G[now]:
        q.append(n)
        ans.append(n)
print(*[i + 1 for i in ans])