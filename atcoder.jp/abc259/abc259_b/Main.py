import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import math
a, b, d = MI()
rad = math.pi / 180 * d
print(*[math.cos(rad) * a - math.sin(rad) * b, math.sin(rad) * a + math.cos(rad) * b])