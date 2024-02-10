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
ans = 0
nl = N
nr = N
kosu = defaultdict(int)
kosu[nl] = 1
def solve(n, a):
    if n % 2 == 1:
        l = n // 2
        r = l + 1
        kosu[l] += a
        kosu[r] += a
    else:
        kosu[n // 2] += a * 2
while nr > 1:
    if nl == nr:
        ans += nl * kosu[nl]
        a = kosu[nl]
        kosu[nl] = 0
        solve(nl, a)
        if nl % 2 == 1:
            nl = nl // 2
            nr = nl + 1
        else:
            nl = nl // 2
            nr = nl
    else:
        ans += nl * kosu[nl] + nr * kosu[nr]
        a = kosu[nl]
        b = kosu[nr]
        kosu[nl] = 0
        kosu[nr] = 0
        solve(nl, a)
        solve(nr, b)
        nl = nl // 2
        nr = nl + 1
    if nl < 2:
        nl = 0
print(ans)