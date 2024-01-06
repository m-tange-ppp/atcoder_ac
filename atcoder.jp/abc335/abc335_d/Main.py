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
ans = [[1] * N for _ in range(N)]
i = 0
j = 0
dir = 0
cnt = 0
change = N - 1
while not (i == (N - 1) // 2 and j == (N - 1) // 2):
    if cnt < 3 *(N - 1) + (N - 2):
        if dir == 0:
            i += 1
            ans[i][j] = ans[i - 1][j] + 1
            cnt += 1
            if i == N - 1:
                dir += 1
        elif dir == 1:
            j += 1
            ans[i][j] = ans[i][j - 1] + 1
            cnt += 1
            if j == N - 1:
                dir += 1
        elif dir == 2:
            i -= 1
            ans[i][j] = ans[i + 1][j] + 1
            cnt += 1
            if i == 0:
                dir += 1
        else:
            j -= 1
            ans[i][j] = ans[i][j + 1] + 1
            cnt += 1
            if j == 1:
                dir = 0
    else:
        if dir == 0:
            i += 1
            ans[i][j] = ans[i - 1][j] + 1
            if ans[i + 1][j] != 1:
                dir += 1
        elif dir == 1:
            j += 1
            ans[i][j] = ans[i][j - 1] + 1
            if ans[i][j + 1] != 1:
                dir += 1
        elif dir == 2:
            i -= 1
            ans[i][j] = ans[i + 1][j] + 1
            if ans[i - 1][j] != 1:
                dir += 1
        else:
            j -= 1
            ans[i][j] = ans[i][j + 1] + 1
            if ans[i][j - 1] != 1:
                dir = 0
for i in range(N):
    if i != (N - 1) // 2:
        print(*ans[i])
    else:
        print(*ans[i][:(N - 1) // 2], "T", *ans[i][(N - 1) // 2 + 1:])
# print(cnt)