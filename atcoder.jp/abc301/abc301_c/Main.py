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

S = si()
T = si()

ATC = list("atcoder")
dicS = defaultdict(int)
dicT = defaultdict(int)
allKeys = set()
divS = 0
divT = 0
for i in range(len(S)):
    dicS[S[i]] += 1
    dicT[T[i]] += 1
    allKeys.update({S[i], T[i]})
for k in allKeys:
    if k != "@":
        div = dicS[k] - dicT[k]
        if div != 0 and not k in ATC:
            print("No")
            sys.exit()
        if div > 0:
            divS += div
        else:
            divT += - div
if dicT["@"] >= divS and dicS["@"] >= divT:
    print("Yes")
else:
    print("No")