#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
from collections import defaultdict, deque
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
Q = ii()

card_num = [[] for _ in range(N + 1)]
box_num = [set() for _ in range(2 * 10 ** 5 + 1)]
for _ in range(Q):
    q = li()
    t = q[0]
    if t == 1:
        c = q[1]
        b = q[2]
        card_num[b].append(c)
        box_num[c].add(b)
    elif t == 2:
        b = q[1]
        card_num[b].sort()
        print(*card_num[b])
    else:
        c = q[1]
        print(*sorted(list(box_num[c])))