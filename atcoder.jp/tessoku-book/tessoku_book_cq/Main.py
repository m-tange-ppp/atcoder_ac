import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, S = MI()
A = LI()
dp = [[-1] * (10001) for _ in range(N + 1)]
dp[0][0] = 1 # これを忘れていた
for i in range(1, N + 1):
    for j in range(10001):
        if 0 <= j - A[i - 1] and dp[i - 1][j - A[i - 1]] == 1:
            dp[i][j] = 1
        elif dp[i - 1][j] == 1:
            dp[i][j] = 1
if dp[N][S] == -1:
    print(-1)
    sys.exit()
else:
    ans_list = []
    i = N
    j = S
    while i > 0:
        if dp[i - 1][j] == -1:
            ans_list.append(i)
            j -= A[i - 1]
        i -= 1
    ans_list.reverse()
    print(len(ans_list))
    print(*ans_list)