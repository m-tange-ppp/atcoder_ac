import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
S = SI()
now = 0
for _ in range(Q):
    t, x = MI()
    if t == 1:
        now = (now + x) % N
    else:
        print(S[((N - now) + x - 1) % N])
