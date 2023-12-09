import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = [0, 0] + LI()
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[i].append(A[i])
ans = [0] * (N + 1)
for i in range(N, 1, -1):
    ans[A[i]] += ans[i] + 1
print(*ans[1:])