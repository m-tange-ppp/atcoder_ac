import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, L = MI()
K = II()
A = LI() + [L]
r = L // (K + 1) + 1
l = 0
mid = (l + r) // 2
while r - l > 1:
    s = 0
    mid = (l + r) // 2
    for i in range(1, K + 2):
        ind = bisect.bisect_left(A, s + mid)
        if ind == N + 1:
            r = mid
            break
        s = A[ind]
    else:
        l = mid
print(l)
