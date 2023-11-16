import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W = MI()
C = [SI() for _ in range(H)]

field = [[0] * W for _ in range(H)]
for i in range(W):
    if C[0][i] == ".":
        field[0][i] = 1
    else:
        break
for i in range(H):
    if C[i][0] == ".":
        field[i][0] = 1
    else:
        break
for i in range(1, H):
    for j in range(1, W):
        if C[i][j] == ".":
            field[i][j] = field[i - 1][j] + field[i][j - 1]
print(field[-1][-1])