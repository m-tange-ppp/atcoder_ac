import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, Q = MI()
R = LI()
R.sort()
R_sum = [R[0]]
for i in range(1, N):
    R_sum.append(R_sum[-1] + R[i])
for _ in range(Q):
    X = II()
    print(bisect.bisect_right(R_sum, X))
