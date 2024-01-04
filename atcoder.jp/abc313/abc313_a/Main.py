import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
P = LI()
if N == 1:
    print(0)
    sys.exit()
saikyo = max(P[1:])
p1 = P[0]
if p1 > saikyo:
    print(0)
else:
    print(saikyo - p1 + 1)