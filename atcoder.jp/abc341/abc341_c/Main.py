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
T = si()
S = [si() for _ in range(H)]

idou = [(0, 0)]
for i in range(len(T)):
    n = idou[-1]
    y, x = n[0], n[1]
    if T[i] == "L":
        x -= 1
    elif T[i] == "R":
        x += 1
    elif T[i] == "U":
        y -= 1
    else:
        y += 1
    idou.append((y, x))
idou = list(set(idou))

ans = 0
for i in range(H):
    for j in range(W):
        y, x = i, j
        for d in idou:
            dy = y + d[0]
            dx = x + d[1]
            if 0 <= dy < H and 0 <= dx < W and S[dy][dx] ==".":
                pass
            else:
                break
        else:
            ans += 1
print(ans)