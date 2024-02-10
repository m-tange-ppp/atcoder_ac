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

N, M = mi()
A = [li(1) for _ in range(M)]
funaka = set()
for i in range(N - 1):
    for j in range(i + 1, N):
        funaka.add((i, j))
for a in A:
    for i in range(N - 1):
        x, y = a[i], a[i + 1]
        if x > y:
            x, y = y, x
        if (x, y) in funaka:
            funaka.remove((x, y))
print(len(funaka))