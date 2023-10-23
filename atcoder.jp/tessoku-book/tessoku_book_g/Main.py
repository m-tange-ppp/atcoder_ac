import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

D = II()
N = II()
imosu = [0] * (D + 1)

for _ in range(N):
    L, R = MI()
    L, R = L - 1, R - 1
    imosu[L] += 1
    imosu[R + 1] -= 1
for i in range(1, D + 1):
    imosu[i] += imosu[i - 1]
    print(imosu[i - 1])