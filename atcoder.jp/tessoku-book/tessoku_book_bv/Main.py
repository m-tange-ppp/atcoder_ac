import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
P = [LI() for _ in range(N)]
row = [max(P[i]) for i in range(N)]
column = [max([P[i][j] for i in range(N)]) for j in range(N)]
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if row[i] > row[j]:
            ans += 1
        if column[i] > column[j]:
            ans += 1
print(ans)