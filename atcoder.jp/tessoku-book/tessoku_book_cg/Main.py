import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
imosu = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
    X, Y = MI()
    imosu[X][Y] += 1
for i in range(1, 1501):
    for j in range(1, 1501):
        imosu[i][j] += imosu[i - 1][j]
for i in range(1, 1501):
    for j in range(1, 1501):
        imosu[i][j] += imosu[i][j - 1]
Q = II()
for _ in range(Q):
    a, b, c, d = MI()
    a -= 1
    b -= 1
    print(imosu[c][d] - imosu[c][b] - imosu[a][d]  + imosu[a][b])