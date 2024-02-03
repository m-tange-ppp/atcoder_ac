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

H, W, N = mi()

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
y = 0
x = 0
now = -1
masu = [["."] * W for _ in range(H)]
for _ in range(N):
    if masu[y][x] == ".":
        masu[y][x] = "#"
        now = (now + 1) % 4
        y = (y + dir[now][0]) % H
        x = (x + dir[now][1]) % W
    else:
        masu[y][x] = "."
        now = (now - 1) % 4
        y = (y + dir[now][0]) % H
        x = (x + dir[now][1]) % W
for k in range(H):
    print("".join(masu[k]))