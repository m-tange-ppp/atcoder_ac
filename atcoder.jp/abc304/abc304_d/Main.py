from bisect import bisect_left, bisect_right
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

W, H = mi()
N = ii()
ichigos = [li() for _ in range(N)]
A = ii()
tates = li()
B = ii()
yokos = li()

pieces = defaultdict(int)
for i in ichigos:
    x = bisect_left(tates, i[0])
    y = bisect_left(yokos, i[1])
    pieces[f"{x},{y}"] += 1
maxi = max(pieces.values())
mini = min(pieces.values())
if len(pieces.keys()) < (A + 1) * (B + 1):
    mini = 0
print(mini, maxi)