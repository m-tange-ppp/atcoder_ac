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

S = si()
cnt = defaultdict(int)
for s in S:
    cnt[s] += 1
cnt_list = []
for v in cnt.values():
    cnt_list.append(v)
cnt_list.sort(reverse=True)
nokori = len(S)
res = 0
idx = 0
while nokori > 0:
    c = cnt_list[idx]
    nokori -= c
    res +=  c * nokori
    idx += 1
if cnt_list[0] != 1:
    res += 1
print(res)