import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
M = [LI() for _ in range(N)]
M.sort(key=lambda x:x[1])
ans = 1
i = 1
a = M[0]
while i < N:
    if a[1] <= M[i][0]:
        a = M[i]
        ans += 1
    i += 1
print(ans)