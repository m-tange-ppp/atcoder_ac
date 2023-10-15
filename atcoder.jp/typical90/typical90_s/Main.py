import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = I()
A_list = LI()

dp = [[-1]*2*N for _ in range(2*N - 1)]

for i in range(1, N + 1):
    for j in range(1, 2*N - 2*(i - 1)):
        if i == 1:
            j = j - 1
            dp[j][j + 1] = abs(A_list[j] - A_list[j + 1])
        else:
            m = float("inf")
            j = j - 1
            for k in range(1, i):
                if dp[j][j + 2*k - 1] + dp[j + 2*k][j + 2*i - 1] < m:
                    m = dp[j][j + 2*k - 1] + dp[j + 2*k][j + 2*i - 1]
            dp[j][j + 2*i - 1] = min(m, dp[j + 1][j + 2*i - 2] + abs(A_list[j] - A_list[j + 2*i - 1]))

print(dp[0][2*N - 1])