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
c = N - 1
cnt = 1
while c >= 2:
    c //= 2
    cnt += 1
print(cnt)
sys.stdout.flush()

j = [[] for _ in range(cnt)]
for i in range(1, N):
    b =  "0" * (cnt - len(bin(i)[2:])) + bin(i)[2:]
    for k in range(cnt):
        if b[k] == "1":
            j[k].append(i)
for juice in j:
    l = len(juice)
    print(l, *juice)
    sys.stdout.flush()

bij = si()
if all(b == "0" for b in bij):
    print(N)
    sys.stdout.flush()
else:
    print(int("0b" + bij, 0))
    sys.stdout.flush()