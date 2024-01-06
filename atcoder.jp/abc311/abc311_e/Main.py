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

H, W, N = mi()
blanks = [li(1) for _ in range(N)]
dp = [[1] * W for _ in range(H)]
for b in blanks:
    i, j = b[0], b[1]
    dp[i][j] = 0
ans = 0
for i in range(-1, H - 1):
    for j in range(-1, W - 1):
        if i == -1 or j == -1:
            pass
        elif dp[i + 1][j + 1] != 0:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        ans += dp[i + 1][j + 1]
print(ans)