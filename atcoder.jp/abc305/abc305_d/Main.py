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

N = ii()
A = li()
sumA = [0]
for i in range(1, N):
    if i % 2 == 0:
        if i == 2:
            sumA.append(A[i] - A[i - 1])
        else:
            sumA.append(A[i] - A[i - 1] + sumA[-1])
Q = ii()
for _ in range(Q):
    res = 0
    l, r = mi()
    indl = bisect_right(A, l)
    indr = bisect_left(A, r)
    if indl % 2 == 0:
        res += A[indl] - l
    if indr % 2 == 0:
        res += r - A[indr - 1]
    res += sumA[(indr - 1) // 2] - sumA[indl // 2]
    print(res)