import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = []
vec = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
max_n = 0
for _ in range(N):
    n = SI()
    a = []
    for i in range(N):
        masu = int(n[i])
        a.append(masu)
        if masu > max_n:
            max_n = masu
    A.append(a)

list_st = []
for i in range(N):
    for j in range(N):
        if A[i][j] == max_n:
            list_st.append((i, j))

ans = 0
for st in list_st:
    for v in vec:
        y, x = st[0], st[1]
        n = A[y][x]
        dy, dx = v[0], v[1]
        for _ in range(0, N - 1):
            y = (y + dy) % N
            x = (x + dx) % N
            n *= 10
            n += A[y][x]
        if n > ans:
            ans = n

print(ans)