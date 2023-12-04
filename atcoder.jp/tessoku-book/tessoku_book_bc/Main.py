import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
Q = II()
L = []
for _ in range(Q):
    q = LI()
    t = q[0]
    x = q[1]
    if t == 1:
        L.append(x)
    elif t == 2:
        L.remove(x)
    else:
        L.sort()
        if bisect.bisect_left(L, x) == len(L):
            print(-1)
        else:
            print(L[bisect.bisect_left(L, x)])