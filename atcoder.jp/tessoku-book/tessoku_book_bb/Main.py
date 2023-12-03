import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
Q = II()
D = defaultdict(int)
for _ in range(Q):
    q = LS()
    t = int(q[0])
    if t == 1:
        D[q[1]] = int(q[2])
    else:
        print(D[q[1]])