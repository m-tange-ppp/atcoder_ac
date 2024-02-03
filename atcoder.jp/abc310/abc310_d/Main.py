#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

N, T, M = mi()
ng = [[] for _ in range(N)]
for _ in range(M):
    a, b = mi(1)
    ng[a].append(b)
    ng[b].append(a)
teams = []
ans = 0
def separate(member: int):
    global ans
    if member == N and len(teams) == T:
        ans += 1
        return
    elif member < N:
        for t in teams:
            if all(not m in t for m in ng[member]):
                t.append(member)
                separate(member + 1)
                t.pop()
        teams.append([member])
        separate(member + 1) # stackで処理するので、リストを引数にせずこれでOK
        teams.pop()
        return
separate(0)
print(ans)