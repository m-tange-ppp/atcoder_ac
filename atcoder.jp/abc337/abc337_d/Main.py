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

H, W, K = mi()
S = [si() for _ in range(H)]
ans = 2 * 10 ** 5 + 1
if K == 1:
    f = False
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                print(0)
                sys.exit()
            elif S[i][j] == ".":
                f = True
    print(1 if f else -1)
else:
    if W >= K:
        for i in range(H):
            l, r = 0, 0
            cnt = 0
            while r < W:
                if S[i][r] == "x":
                    l = r + 1
                    r += 1
                    cnt = 0
                elif S[i][r] == "o":
                    if r - l + 1 < K:
                        r += 1
                    else:
                        r += 1
                        l += 1
                        if S[i][l - 1] == ".":
                            cnt -= 1
                else:
                    if r - l + 1 < K:
                        r += 1
                        cnt += 1
                    else:
                        r += 1
                        l += 1
                        cnt += 1
                        if S[i][l - 1] == ".":
                            cnt -= 1
                if r < W and r - l + 1 == K:
                    if S[i][r] == ".":
                        ans = min(ans, cnt + 1)
                    elif S[i][r] == "o":
                        ans = min(ans, cnt)
    if H >= K:
        for i in range(W):
            l, r = 0, 0
            cnt = 0
            while r < H:
                if S[r][i] == "x":
                    l = r + 1
                    r += 1
                    cnt = 0
                elif S[r][i] == "o":
                    if r - l + 1 < K:
                        r += 1
                    else:
                        r += 1
                        l += 1
                        if S[l - 1][i] == ".":
                            cnt -= 1
                else:
                    if r - l + 1 < K:
                        r += 1
                        cnt += 1
                    else:
                        r += 1
                        l += 1
                        cnt += 1
                        if S[l - 1][i] == ".":
                            cnt -= 1
                if r < H and r - l + 1 == K:
                    if S[r][i] == ".":
                        ans = min(ans, cnt + 1)
                    elif S[r][i] == "o":
                        ans = min(ans, cnt)
    print(ans if ans != 2 * 10 ** 5 + 1 else -1)