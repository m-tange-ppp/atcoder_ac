import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
T = SI()
M = len(S)
N = len(T)

dp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    f = True
    for j in range(1, N + 1):
        if S[i - 1] == T[j - 1] and f:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[M][N])