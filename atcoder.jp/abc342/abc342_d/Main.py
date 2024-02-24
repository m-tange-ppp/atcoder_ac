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
A = li()

ans = 0
sq = []
for i in range(2  * 10 ** 5 + 1):
    sq.append(i ** 2)
nokori = defaultdict(int)
kouho = set()
for i in range(N):
    a = A[i]
    idx = 1
    n = a
    while sq[idx] <= a:
        if a % sq[idx] == 0:
            n = a // sq[idx]
        idx += 1
    nokori[n] += 1
    kouho.add(n)
for k in list(kouho):
    cnt = nokori[k]
    if k == 0:
        ans += N * (N - 1) // 2 - (N - cnt) * (N - cnt - 1) // 2
    else:
        ans += cnt * (cnt - 1) // 2
print(ans)