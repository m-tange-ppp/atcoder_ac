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

N = ii()
A = li()

res = []
for i in range(N - 1):
    div = A[i + 1] - A[i]
    res.append(A[i])
    if div > 0:
        for j in range(div - 1):
            res.append(A[i] + j + 1)
    else:
        for j in range(- div - 1):
            res.append(A[i] - (j + 1))
res.append(A[-1])
print(*res)