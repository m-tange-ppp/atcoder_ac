from bisect import bisect_left, bisect_right
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

N = ii()
A = li()
S = si()
ms = [[0, 0, 0] for _ in range(N)]
eInd = []
xs = [[0, 0, 0] for _ in range(N)]

if S[0] == 'M':
    ms[0][A[0]] += 1
if S[-1] == 'X':
    xs[-1][A[-1]] += 1

for i in range(N - 1):
    ms[i + 1] = [ms[i][0], ms[i][1], ms[i][2]]
    if S[i + 1] == 'M':
        ms[i + 1][A[i + 1]] += 1
    elif S[i + 1] == 'E' and i + 1 < N - 1:
        eInd.append(i + 1)

for i in range(N - 1, 0, -1):
    xs[i - 1] = [xs[i][0], xs[i][1], xs[i][2]]
    if S[i - 1] == 'X':
        xs[i - 1][A[i - 1]] += 1

ans = 0
for e in eInd:
    for i in range(3):
        for j in range(3):
            for p in range(4):
                if p != A[e] and p != i and p != j:
                    ans += p * ms[e - 1][i] * xs[e + 1][j]
                    break

print(ans)
