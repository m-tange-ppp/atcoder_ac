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
S = list(si())
code = [[i] for i in range(26)]
for i in range(N):
    c = ord(S[i]) - ord("a")
    code[c].append(i)
Q = ii()
for _ in range(Q):
    c, d = sys.stdin.readline().rstrip().split()
    l = ord(c) - ord("a")
    r = ord(d) - ord("a")
    for i in range(26):
        if code[i][0] == l:
            code[i][0] = r
ans = [""] * N
for i in range(26):
    for c in code:
        if c[0] == i:
            for j in range(1, len(c)):
                ans[c[j]] = chr(i + ord("a"))
print("".join(ans))
