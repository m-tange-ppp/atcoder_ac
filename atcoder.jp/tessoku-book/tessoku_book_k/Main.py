import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, X = MI()
A = LI()
l = -1
r = N
while r - l > 1:
    mid = (l + r) // 2
    if X < A[mid]:
        r = mid
    else:
        l = mid
print(r)