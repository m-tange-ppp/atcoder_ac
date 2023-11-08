import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import math
N = II()
P = [0] + LI()
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][1] = P[1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        if j == 1:
            dp[i][j] = max(dp[i - 1][j], P[i])
        elif 2 <= j <= i - 1:
            dp[i][j] = max(dp[i - 1][j], 0.9 * dp[i - 1][j - 1] + P[i])
        else:
            dp[i][j] = 0.9 * dp[i - 1][j - 1] + P[i]
measure = [0, 1]
for _ in range(N - 1):
    measure.append(measure[-1] * 0.9 + 1)
ans = - 10 ** 9
for i in range(1, N + 1):
    for j in range(1, i + 1):
        r = dp[i][j] / measure[j] - 1200 / math.sqrt(j)
        if ans < r:
            ans = r
print(ans)