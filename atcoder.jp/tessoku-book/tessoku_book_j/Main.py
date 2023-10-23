import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
D = II()
A_ind = []
for i in range(N):
    A_ind.append([A[i], i])
A_ind.sort(key=lambda x:x[0], reverse=True)
for _ in range(D):
    L, R = MI()
    L, R = L - 1, R - 1
    i = 0
    while True:
        a = A_ind[i]
        if not L <= a[1] <= R:
            print(a[0])
            break
        i += 1