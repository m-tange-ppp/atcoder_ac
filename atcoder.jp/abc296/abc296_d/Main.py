#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd
#from heapq import heapify, heappush, heappop
import sys
from math import ceil
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
INF=float('inf'); MOD=998244353 #10**9+7

N, M = mi()

if N ** 2 < M:
    print(-1)
    sys.exit()
elif M <= N:
    print(M)
    sys.exit()
sqm = ceil(M ** 0.5)
ans = INF
for i in range(1, sqm + 1):
    if i * ceil(M / i) >= M and ceil(M / i) <= N:
        ans = min(ans, i * ceil(M / i))
print(ans)