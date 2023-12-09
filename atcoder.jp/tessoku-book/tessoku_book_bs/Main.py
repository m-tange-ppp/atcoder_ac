import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
B = LI()
A.sort()
B.sort(reverse=True)
ans = 0
for i in range(N):
    ans += A[i] * B[i]
print(ans)