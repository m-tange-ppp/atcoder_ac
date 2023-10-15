import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = I()
s = S()

ans = 0
zero, one = 0, 0 

for i in range(N):
    n = int(s[i])
    if n == 0:
        zero, one = 0, zero + one
        zero += 1
    else:
        zero, one = one, zero
        one += 1
    ans += one

print(ans)