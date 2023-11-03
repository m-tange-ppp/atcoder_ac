import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, W = MI()
A = []
for _ in range(N):
    A.append(LI())
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        if A[i - 1][0] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1][0]] + A[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][W])