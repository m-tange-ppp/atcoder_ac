import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import math
N, K = MI()
A = LI()
A.sort(reverse=True)
P = [LI() for _ in range(N)]
K = [P.pop(a - 1) for a in A]
ans = 0
for p in P:
    min_p = 10 ** 6
    for k in K:
        d = math.sqrt((p[0] - k[0])**2 + (p[1] - k[1])**2)
        if d < min_p:
            min_p = d
    if ans < min_p:
        ans = min_p
print(ans)