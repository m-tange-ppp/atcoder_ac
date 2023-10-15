import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

import copy
N = I()
A = [list(S()) for _ in range(N)]
B = copy.deepcopy(A)

for i in range(1, N):
    B[0][i] = A[0][i - 1]
    B[i][N - 1] = A[i - 1][N - 1]
    B[N - 1][i - 1] = A[N - 1][i]
    B[i - 1][0] = A[i][0]

gen =["".join(r)for r in B]
for g in gen:
    print(g)