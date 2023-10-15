import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, X = MI()
A = LI()
A.sort()
max_A = max(A)
min_A = min(A)
sum_A = sum(A)
now = sum_A - min_A - max_A
f = True
ans = 0
if now + min_A >= X:
    ans = 0
    f = False
else:
    for i in range(min_A + 1, max_A + 1):
        new = now + i
        if now + i >= X:
            ans = i
            f = False
            break
if f:
    ans = -1
print(ans)