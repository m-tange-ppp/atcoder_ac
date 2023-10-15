import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
senkyoku = []
S = 0
for _ in range(N):
    X, Y, Z = mi()
    cost = max((X + Y + 1) // 2 - X, 0)
    senkyoku.append((cost, Z))
    S += Z

W = (S + 1) // 2
dp = [[sum(x[0] for x in senkyoku)] * (W) for _ in range(N + 1)]

for i in range(N):
    for j in range(W):
        if j < senkyoku[i][1]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - senkyoku[i][1]] - senkyoku[i][0])
print(dp[N][W - 1])