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
Q = li()
A = li()
B = li()

l = -1
r = 2 * 10 ** 6 + 1
def check(n):
    for i in range(n + 1):
        if all(A[j] * i + B[j] * (n - i) <= Q[j] for j in range(N)):
            return True
    return False

while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
