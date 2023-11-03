import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N = II()
A = [0] + LI()
B = [0] + LI()

dp = [-1] * (N + 1)
dp[1] = 0
for i in range(1, N):
    if dp[i] >= 0:
        dp[A[i]] = max(dp[A[i]], dp[i] + 100)
        dp[B[i]] = max(dp[B[i]], dp[i] + 150)

print(dp[N])