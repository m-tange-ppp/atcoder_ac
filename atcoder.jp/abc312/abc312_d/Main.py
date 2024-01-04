import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
MOD = 998244353
if len(S) % 2 != 0:
    print(0)
    sys.exit()
dp = [[0] * (len(S) // 2 + 1) for _ in range(len(S) + 1)]
dp[0][0] = 1
for i in range(1, len(S) + 1):
    for j in range(len(S) // 2 + 1):
        if S[i - 1] == "(" and 1 <= j:
            dp[i][j] = dp[i - 1][j - 1]
        elif S[i - 1] == ")" and j <= len(S) // 2 - 1:
            dp[i][j] = dp[i - 1][j + 1]
        elif S[i - 1] == "?":
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == len(S) // 2:
                dp[i][j] = dp[i - 1][j - 1]
            elif 0 < j < len(S) // 2:
                dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]
print(dp[len(S)][0] % MOD)