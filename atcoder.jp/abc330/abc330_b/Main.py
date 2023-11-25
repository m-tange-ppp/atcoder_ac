import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, L, R = MI()
A = LI()
ans = [0] * N
for i, a in enumerate(A):
    if a <= L:
        ans[i] = L
    elif L < a < R:
        ans[i] = a        
    else:
        ans[i] = R
print(*ans)