import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
A.reverse()
count = 0
koma = A[0]
while koma < 4 and count < N:
    count += 1
    if count < N:
        koma += A[count]
print(N - count)