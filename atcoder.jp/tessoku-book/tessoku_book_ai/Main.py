import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
dp = [[0] * (N+1) for _ in range(N+1)]
dp[N] = A
for i in range(N - 1, 0, -1):
    for j in range(i):
        if i % 2 == 1:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        if i % 2 == 0:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])
print(dp[1][0])