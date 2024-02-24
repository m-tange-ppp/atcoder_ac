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

S = si()
x = -1
y = -1
for i in range(8):
    if S[i] == "B":
        if x == -1:
            x = i % 2
        else:
            y = i % 2
if x == y:
    print("No")
    sys.exit()

idx = S.index("K")
if "R" in S[:idx] and "R" in S[idx + 1:]:
    print("Yes")
else:
    print("No")