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
N = min(H, W)
C = [si() for _ in range(H)]
cnt = [0] * N

for i in range(H):
    for j in range(W):
        if ((i == 0 or j == 0) or (i - 1 >= 0 and j - 1 >= 0
            and C[i - 1][j - 1] == ".")) and C[i][j] == "#":
            if i + 1 < H and j + 1 < W and C[i + 1][j + 1] == "#":
                y = i + 1
                x = j + 1
                c = 0
                while True:
                    if C[y - 1][x + 1] == "#":
                        break
                    c += 1
                    y += 1
                    x += 1
                cnt[c] += 1
print(*cnt)