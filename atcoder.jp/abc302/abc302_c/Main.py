#from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
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

N, M = mi()
S = [si() for _ in range(N)]

orders = list(permutations([i for i in range(N)]))
for o in orders:
    for i in range(N - 1):
        l = S[o[i]]
        r = S[o[i + 1]]
        cnt = 0
        for j in range(M):
            if l[j] != r[j]:
                cnt += 1
        if cnt != 1:
            break
    else:
        print("Yes")
        sys.exit()
print("No")