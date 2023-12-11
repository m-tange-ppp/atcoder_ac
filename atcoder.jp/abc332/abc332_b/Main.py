import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

K, G, M = MI()
g = 0
m = 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if m >= G - g:
            m -= G - g
            g = G
        else:
            g += m
            m = 0
print(g, m)