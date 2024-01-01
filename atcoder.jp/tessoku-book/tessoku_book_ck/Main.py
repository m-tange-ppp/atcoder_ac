import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from fractions import Fraction
N = II()
l = 0
r = N
while r - l > 0.0001:
    mid = Fraction(l + r, 2)
    if mid ** 3 + mid <= N:
        l = mid
    else:
        r = mid
print(float(l))