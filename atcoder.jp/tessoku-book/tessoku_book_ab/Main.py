import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
ans = 0
for _ in range(N):
    a = LS()
    T, A = a[0], int(a[1])
    if T == "+":
        ans += A
    elif T == "-":
        ans -= A
    else:
        ans *= A
    ans %= 10000
    print(ans)