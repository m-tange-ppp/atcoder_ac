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

N = ii()
l = defaultdict(int)
r = defaultdict(int)
for i in range(1, N + 1):
    a, b = li()
    if a > b:
        a, b = b, a
    l[a] = i
    r[b] = i

s = deque()
for i in range(1, 2 * N + 1):
    if l[i] != 0:
        s.append(l[i])
    else:
        ind = s.pop()
        if ind != r[i]:
            print("Yes")
            sys.exit()
print("No")