#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

N, M, K = mi()

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

l = lcm(N, M)
waru = l // N + l // M - 2
sho = (K - 1) // waru
amari = (K - 1) % waru
ll = 0
rr = l + 1

def check(x):
    if x // N + x // M <= amari:
        return True
    return False
while rr - ll > 1:
    mid = (ll + rr) // 2
    if check(mid):
        ll = mid
    else:
        rr = mid
c = max(ll // N * N, ll // M * M)
print(l * sho + rr)
# print(l)
# print(waru)
# print(sho)
# print(amari)