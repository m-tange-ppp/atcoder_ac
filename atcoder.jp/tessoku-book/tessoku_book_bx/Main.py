import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, W, L, R = MI()
X = [0] + LI() + [W]
MOD = 1000000007

dp = [0] * (N + 2)
dp_sum = [0] * (N + 2)
for i in range(1, N + 2):
    now = X[i]
    l = max(bisect.bisect_left(X, now - R) - 1, 0)
    r = bisect.bisect_right(X, max(now - L, 0)) - 1
    if L <= now <= R:
        dp[i] += 1
    dp[i] += dp_sum[r] - dp_sum[l]
    dp_sum[i] = dp_sum[i - 1] + dp[i]
print(dp[-1] % MOD)