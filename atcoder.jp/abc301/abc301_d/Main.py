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

S = si()
N = ii()
L = len(S)

minb = 0
ans = 0
for i in range(L):
    if S[i] == "1":
        minb += 2 ** (L - 1 - i)
if N < minb:
    print(-1)
    sys.exit()
ans = minb
for i in range(L):
    if N >= 2 ** (L - 1 - i) + ans and S[i] == "?":
        ans += 2 ** (L - 1 - i)
print(ans)