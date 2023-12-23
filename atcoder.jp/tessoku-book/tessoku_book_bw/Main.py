import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
E = [LI() for _ in range(N)]
E.sort(key=lambda x:x[1])
max_D = max([x[1] for x in E])
dp = [[0] * (max_D + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    exam = E[i - 1]
    for j in range(1, max_D + 1):
        if exam[0] <= j <= exam[1]:
            dp[i][j] = max(dp[i - 1][j - exam[0]] + 1, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(max(dp[N]))