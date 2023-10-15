import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K, Q = MI()
A = LI()
L = LI()

for l in L:
    ind = l - 1
    if ind == K - 1:
        if A[ind] != N:
            A[ind] += 1
    else:
        if A[ind + 1] - A[ind] > 1:
            A[ind] += 1

print(*A)