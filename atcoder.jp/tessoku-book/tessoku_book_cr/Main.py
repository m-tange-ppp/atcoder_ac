import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, W = MI()
A = [LI() for _ in range(N)]
dp = [[W + 1] * (10 ** 5 + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(10 ** 5 + 1):
        w, v = A[i - 1]
        if j - v >= 0:
            kouho = min(dp[i - 1][j - v] + w, dp[i - 1][j])
            if kouho <= W:
                dp[i][j] = kouho
        else:
            dp[i][j] = dp[i - 1][j]
ans = 0
for  i in range(10 ** 5 + 1):
    if dp[N][i] <= W:
        ans = i
print(ans)