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

Q = ii()
dic = defaultdict(int)
keys_size = 0

for _ in range(Q):
    query = li()
    if query[0] == 3 :
        t = 0
    else:
        t, x = query[0], query[1]
    
    if t == 1:
        if dic[x] == 0:
            keys_size += 1
        dic[x] += 1
    elif t == 2:
        dic[x] -= 1
        if dic[x] == 0:
            keys_size -= 1
    else:
        print(keys_size)

    