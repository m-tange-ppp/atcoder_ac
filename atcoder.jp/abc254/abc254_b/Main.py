import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = [[] for _ in range(N)]
A[0] = [1]
for i in range(1, N):
    A[i].append(1)
    for j in range(i - 1):
        A[i].append(A[i - 1][j] + A[i - 1][j + 1])
    A[i].append(1)
for a in A:
    print(*a)