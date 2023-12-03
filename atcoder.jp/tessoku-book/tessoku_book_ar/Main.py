import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
A = [i + 1 for i in range(N)]
rev = False
for _ in range(Q):
    q = LI()
    num = q[0]
    if num == 1:
        ind, value = q[1] - 1, q[2]
        if not rev:
            A[ind] = value
        else:
            A[N - 1 - ind] = value 
    elif num == 2:
        rev = not rev
    else:
        ind = q[1] - 1
        if not rev:
            print(A[ind])
        else:
            print(A[N - 1 - ind])