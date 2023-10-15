import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, Q = MI()
A = LI()
A.sort()
sum_A = [A[0]]
for i in range(N - 1):
    sum_A.append(sum_A[i] + A[i + 1])
for _ in range(Q):
    X = II()
    ind = bisect.bisect_right(A, X)
    if ind == 0:
        ans = sum_A[-1] - X * N
    elif ind == N:
        ans = X * N - sum_A[-1]
    else:
        l = X * ind - sum_A[ind - 1]
        r = sum_A[-1] - sum_A[ind - 1] - X *(N - ind)
        ans = l + r
    print(ans)
