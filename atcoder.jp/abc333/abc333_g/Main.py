import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from fractions import Fraction
R = input()
r = Fraction(R) - Fraction(1, 10 ** 50)
n = int(input())
ans = r.limit_denominator(n)
print(ans.numerator, ans.denominator)