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

N, M, H, K = mi()
S = si()
items = set()
now = [0, 0]
for _ in range(M):
    x, y = mi()
    items.add((x, y))
for i in range(N):
    if S[i] == "R":
        now = [now[0] + 1, now[1]]
    elif S[i] == "L":
        now = [now[0] - 1, now[1]]
    elif S[i] == "U":
        now = [now[0], now[1] + 1]
    else:
        now = [now[0], now[1] - 1]
    H -= 1
    if H < 0:
        print("No")
        sys.exit()
    if H < K and tuple(now) in items:
        items.remove(tuple(now))
        H = K
print("Yes")