import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
N = II()
A = LI()
av = sum(A) // N
if sum(A) % N == 0:
    ans = 0
    for a in A:
        if a - av > 0:
            ans += a - av
    print(ans)
else:
    avl, avr = av, av + 1
    l = 0
    r = 0
    for a in A:
        if a <= avl:
            l += avl - a
        else:
            r += a - avr
    print(max(l, r))