import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,Q = MI()
P = [SI() for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        if P[i-1][j-1] == "B":
            dp[i][j] += 1

sq = dp[-1][-1]

def calc(y, x):
    return sq*(y//N)*(x//N) + dp[y%N][N]*(x//N) + dp[N][x%N]*(y//N) + dp[y%N][x%N]

for _ in range(Q):
    A,B,C,D = MI()
    A,B,C,D = A+1,B+1,C+1,D+1
    print(calc(C,D) - calc(C,B-1) - calc(A-1,D) + calc(A-1,B-1))

