import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

X, A, D, N = MI()
ans = 0
if D < 0:
    if X > A:
        ans = X - A
    elif X < A + (N - 1) * D:
        ans = (A + (N - 1) * D) - X
    else:
        abs_D = abs(D)
        mod = (X - A) % abs_D
        ans = min(abs_D - mod, mod)
elif D == 0:
    ans = abs(X - A)
else:
    if X < A:
        ans = A - X
    elif X > A + (N - 1) * D:
        ans = X - (A + (N - 1) * D)
    else:
        mod = (X - A) % D
        ans = min(D - mod, mod)
print(ans)