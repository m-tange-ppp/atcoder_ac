#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
# from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

N, Q = mi()
dragon = [[N - x, 0] for x in range(N)]
for _ in range(Q):
    q, c = sys.stdin.readline().rstrip().split()
    if q == "1":
        x, y = dragon[-1][0], dragon[-1][1]
        if c == "R":
            dragon.append([x + 1, y])
        elif c == "L":
            dragon.append([x - 1, y])
        elif c == "U":
            dragon.append([x, y + 1])
        else:
            dragon.append([x, y - 1])
        # print(dragon)
    else:
        print(*dragon[-int(c)])
