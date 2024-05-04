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

W, B = mi()
P = []
K = "wbwbwwbwbwbw"
for i in range(12):
    cw = 0
    cb = 0
    for j in range(i + 1):
        if K[j] == "w":
            cw += 1
        else:
            cb += 1
    P.append([cw, cb])
N = W + B
sho = (N - 1) // 12
amari = (N - 1) % 12
w = sho * 7 + P[amari][0]
b = sho * 5 + P[amari][1]
flag = False
if W == w and B == b:
    flag = True
for i in range(12):
    w -= 1 if K[i] == "w" else 0
    b -= 1 if K[i] == "b" else 0
    amari = (amari + 1) % 12
    if amari == 0:
        w += P[amari][0]
        b += P[amari][1]
    else:
        w += P[amari][0] - P[amari - 1][0]
        b += P[amari][1] - P[amari - 1][1]
    if W == w and B == b:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")