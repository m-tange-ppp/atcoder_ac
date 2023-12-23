import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A, M, L, R = MI()
ln = 0
rn = 0
while True:
    if (L - A) % M == 0:
        ln = (L - A) // M
        break
    L += M - (L - A) % M
while True:
    if (R - A) % M == 0:
        rn = (R - A) // M
        break
    R -= (R - A) % M
print(rn - ln + 1)