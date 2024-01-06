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

N = ii()
x, y, z = 0, 0, 0
while x < N:
    print(x, y, z)
    if x + y + z < N:
        z += 1
    elif x + y + z == N and z > 0:
        y += 1
        z = 0
    elif x + y + z == N and z == 0:
        x += 1
        y = 0
print(x, y, z)