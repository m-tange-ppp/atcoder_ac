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
A = [li() for _ in range(N)]
B = [li() for _ in range(N)]

spin = [A]
for _ in range(3):
    s = [[0] * N for _ in range(N)]
    f = spin[-1]
    for i in range(N):
        for j in range(N):
            s[i][j] = f[j][N - 1 - i]
    spin.append(s)
for s in spin:
    for i in range(N):
        for j in range(N):
            if s[i][j] == 1 and B[i][j] != 1:
                break
        else:
            continue
        break
    else:
        print("Yes")
        sys.exit()
print("No")