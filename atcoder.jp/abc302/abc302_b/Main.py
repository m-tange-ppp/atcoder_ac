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

H, W = mi()
S = [si() for _ in range(H)]

dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
snuke = ["s", "n", "u", "k", "e"]
def search(i, j):
    for d in dirs:
        for k in range(5):
            di = i + d[0] * k
            dj = j + d[1] * k
            if 0 <= di < H and 0 <= dj < W and S[di][dj] == snuke[k]:
                pass
            else:
                break
        else:
            res = []
            for l in range(5):
                res.append([i + d[0] * l, j + d[1] * l])
            return res
    return False


for i in range(H):
    for j in range(W):
        if search(i, j):
            ans = search(i, j)
            for k in range(5):
                print(ans[k][0] + 1, ans[k][1] + 1)