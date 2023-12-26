import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
imosu = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
    A, B, C, D = MI()
    imosu[A][B] += 1
    imosu[A][D] -= 1
    imosu[C][B] -= 1
    imosu[C][D] += 1
for i in range(1, 1501):
    for j in range(1501):
        imosu[i][j] += imosu[i - 1][j]
for i in range(1501):
    for j in range(1, 1501):
        imosu[i][j] += imosu[i][j - 1]
for i in range(1501):
    for j in range(1501):
        imosu[i][j] = 1 if imosu[i][j] > 0 else 0
print(sum([sum(a) for a in imosu]))