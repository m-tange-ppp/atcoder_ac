from bisect import bisect_left, bisect_right
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

N, M, D = mi()
A = li()
B = li()

A.sort()
B.sort()
ans = -1
for a in A:
    idx = bisect_left(B, a + D)
    if 0 <= idx < M and B[idx] - a <= D:
        ans = max(ans, a + B[idx])
    elif 0 <= idx - 1 < M and abs(a - B[idx - 1]) <= D:
        ans = max(ans, a + B[idx - 1])
print(ans)
