import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, S, K = MI()
L = [LI() for _ in range(N)]
ans = 0
for a in L:
    ans += a[0] * a[1]
if ans < S:
    ans += K
print(ans)