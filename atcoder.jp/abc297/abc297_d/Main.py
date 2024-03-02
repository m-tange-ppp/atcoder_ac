#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
from math import gcd
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
INF=float('inf'); MOD=998244353 #10**9+7

def calc(a, b):
    if a < b:
        a, b = b, a
    return a % b, b, a // b

A, B = mi()
ans = 0
a, b = A, B
while a != b and (a != 0 and b != 0):
    a, b, c = calc(a, b)
    ans += c
if ans > 0:
    ans -= 1
print(ans)
