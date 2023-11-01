import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = [0] + LI()
mod = 998244353
p = pow(N, mod - 2, mod)
dp = [0] * (N + 1)
dp[N] = A[N]
sum_dp = [0] * (N + 1)
sum_dp[N] = A[N]
for i in range(N - 1, -1, -1):
    dp[i] = (A[i] + sum_dp[i + 1] * p) % mod
    sum_dp[i] = (sum_dp[i + 1] + dp[i]) % mod
print(dp[0] % mod)
    