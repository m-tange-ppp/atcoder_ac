import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
A = LI()
sum_A = [A[0]]
for i in range(1, N):
    sum_A.append(sum_A[-1] + A[i])
for _ in range(Q):
    L, R = MI()
    L, R = L - 1, R - 1
    if L == 0:
        print(sum_A[R])
    else:
        print(sum_A[R] - sum_A[L - 1])
