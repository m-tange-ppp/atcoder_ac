import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

T = II()
N = II()
imosu = [0] * (T + 1)
for _ in range(N):
    L, R = MI()
    imosu[L] += 1
    imosu[R] -= 1
for i in range(1, T + 1):
    imosu[i] += imosu[i - 1]
for a in imosu[:-1]:
    print(a)