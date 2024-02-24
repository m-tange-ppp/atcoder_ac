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
S = si()

ans = -1
cnt = 0
l = 0
for i in range(N):
    if S[i] == "o" and i < N - 1:
        cnt += 1
    elif S[i] == "o" and i == N - 1:
        cnt += 1
        if l > 0:
            ans = max(ans, cnt)
    else:
        if cnt != 0:
            ans = max(ans, cnt)
        l = i + 1
        cnt = 0
print(ans)
