import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W, N = MI()
ans = [[0] * (W + 1) for _ in range(H + 1)]
for _ in range(N):
    A, B, C, D = MI()
    ans[A - 1][B - 1] += 1
    ans[A - 1][D] -= 1
    ans[C][B - 1] -= 1
    ans[C][D] += 1

for i in range(H + 1):
    for j in range(1, W + 1):
        ans[i][j] += ans[i][j - 1]
for j in range(W + 1):
    for i in range(1, H + 1):
        ans[i][j] += ans[i - 1][j]

for i in range(H):
    print(*ans[i][:-1])
