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

H, W = mi()
S = [si() for _ in range(H)]
l = 1000
r = 0
t = 1000
b = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            l = min(l, j)
            r = max(r, j)
            t = min(t, i)
            b = max(b, i)
for i in range(t, b + 1):
    for j in range(l, r + 1):
        if S[i][j] == ".":
            print(i + 1, j + 1)