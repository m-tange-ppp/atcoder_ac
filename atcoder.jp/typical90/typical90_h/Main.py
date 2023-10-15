N = int(input())
S = list(input())
atcoder = "atcoder"
dp = [[0]*(len(atcoder) + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(len(atcoder) + 1):
        dp[i + 1][j] = dp[i][j] + dp[i + 1][j]
        if j < len(atcoder) and S[i] == atcoder[j]:
            dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j + 1]

print(dp[N][len(atcoder)] % (10 ** 9 + 7))