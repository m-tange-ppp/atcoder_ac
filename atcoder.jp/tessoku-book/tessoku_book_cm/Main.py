import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, K = MI()
A = LI()
L = A[:N // 2]
R = A[N // 2:]
sum_L = []
sum_R = set()
for i in range(2 ** (len(L))):
    s = 0
    for j in range(len(L)):
        if i & (1 << j):
            s += L[j]
    sum_L.append(s)
for i in range(2 ** (len(R))):
    s = 0
    for j in range(len(R)):
        if i & (1 << j):
            s += R[j]
    sum_R.add(s)
for l in sum_L:
    if K - l in sum_R:
        print("Yes")
        sys.exit()
else:
    print("No")