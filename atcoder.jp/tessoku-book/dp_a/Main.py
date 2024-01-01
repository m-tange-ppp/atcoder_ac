import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
H = LI()
dp = [0] * N
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(H[i - 2] - H[i]), dp[i - 1] + abs(H[i - 1] - H[i]))
print(dp[N - 1])