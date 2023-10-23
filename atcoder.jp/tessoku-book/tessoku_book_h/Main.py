import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W = MI()
X = [LI() for _ in range(H)]
Q = II()

sum_X = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if j == 1:
            sum_X[i][j] = X[i - 1][j - 1]
        else:
            sum_X[i][j] = sum_X[i][j - 1] + X[i - 1][j - 1]
for j in range(1, W + 1):
    for i in range(2, H + 1):
        sum_X[i][j] += sum_X[i - 1][j]

for _ in range(Q):
    A, B, C, D = MI()
    print(sum_X[C][D] - sum_X[A - 1][D] - sum_X[C][B - 1] + sum_X[A - 1][B - 1])