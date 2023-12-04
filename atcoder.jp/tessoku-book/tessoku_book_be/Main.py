import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
A = LI()
for i in range(N):
    A[i] -= 1

dp = [[0] * N for _ in range(36)]
for j in range(N):
    dp[0][j] = A[j]
for i in range(1, 36):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]] #doublingのテーブル更新

for _ in range(Q):
    X, Y = MI()
    X -= 1
    ans = X
    i = 0
    while Y:
        if Y & 1:
            ans = dp[i][ans]
        Y >>= 1
        i += 1
    print(ans + 1)