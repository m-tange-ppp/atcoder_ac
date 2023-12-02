import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

M,D = MI()
y,m,d = MI()
d += 1
if d > D:
    d = 1
    m = m+1
    if m > M:
        m = 1
        y += 1
print(f"{y} {m} {d}")