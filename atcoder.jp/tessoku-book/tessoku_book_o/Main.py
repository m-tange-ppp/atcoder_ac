import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()

ind_a = []
for i, a in enumerate(A):
    ind_a.append([i, a])
ind_a.sort(key=lambda x:x[1])
f = False
for i in range(N):
    if i == 0:
        if N != 1 and ind_a[i][1] == ind_a[i + 1][1]:
            f = True
        ind_a[i][1] = 1
    else:
        a = ind_a[i][1]
        if f:
            ind_a[i][1] = ind_a[i - 1][1]
        else:
            ind_a[i][1] = ind_a[i - 1][1] + 1
        if i < N - 1:
            if a == ind_a[i + 1][1]:
                f = True
            else:
                f = False
ind_a.sort(key=lambda x:x[0])
print(*[x[1] for x in ind_a])