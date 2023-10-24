import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
A = LI()

l = 0
r = 10 ** 9 + 1
def maisu(t):
    n = 0
    for a in A:
        n += t // a
    return n
        
while r - l > 1:
    mid = (l + r) // 2
    if K > maisu(mid):
        l = mid
    else:
        r = mid

print(r)