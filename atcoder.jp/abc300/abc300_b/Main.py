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
A = [si() for _ in range(H)]
B = [si() for _ in range(H)]

for i in range(H):
    for j in range(W):
        t = [["0"] * W for _ in range(H)]
        for k in range(H):
            for l in range(W):
                t[k][l] = A[(k + i) % H][(l + j) % W]
        if all(t[i][j] == B[i][j] for i in range(H) for j in range(W)):
            print("Yes")
            sys.exit()
print("No")