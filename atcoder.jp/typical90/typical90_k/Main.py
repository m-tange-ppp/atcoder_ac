N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
works.sort(key=lambda x:x[0])

dp = [[0]*(N + 1) for _ in range(max(w[0] for w in works) + 1)]

for n in range(len(dp[0])):
    for d in range(len(dp)):
        if n > 0 and d > 0:
            if works[n - 1][1] <= d <= works[n - 1][0]:
                dp[d][n] = max(works[n - 1][2] + dp[d -works[n - 1][1]][n - 1], dp[d - 1][n], dp[d][n - 1])
            else:
                dp[d][n] = max(dp[d - 1][n], dp[d][n - 1])

print(dp[d][n])
