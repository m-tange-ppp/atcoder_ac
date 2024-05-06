#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
INF=float('inf'); MOD=998244353 #10**9+7

N, A, B = mi()
D = li()

C = A + B
mod = list(set(d % C for d in D))
mod.sort()
m = mod[0]
M = mod[-1]
flag = False
if M - m < A:
    flag = True
else:
    for i in range(1, len(mod)):
        m = mod[i]
        M = mod[i - 1] + C
        if M - m < A:
            flag = True
            break
if flag:
    print("Yes")
else:
    print("No")
