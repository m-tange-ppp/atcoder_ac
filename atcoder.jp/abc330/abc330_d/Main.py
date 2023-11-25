import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
S = [SI() for _ in range(N)]
yoko_maru = [0] * N
tate_maru = [0] * N
for i in range(N):
    yoko_maru[i] = (S[i].count("o"))
    c = 0
    for j in range(N):
        if S[j][i] == "o":
            c += 1
    tate_maru[i] = c

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            ans += (yoko_maru[i] - 1) * (tate_maru[j] - 1)
print(ans)