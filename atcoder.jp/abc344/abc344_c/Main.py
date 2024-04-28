#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
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
M = ii()
B = li()
L = ii()
C = li()
Q = ii()
X = li()

res = set()
for i in range(N):
    for j in range(M):
        for k in range(L):
            res.add(A[i] + B[j] + C[k])
for x in X:
    if x in res:
        print("Yes")
    else:
        print("No")