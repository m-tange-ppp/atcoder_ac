import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
A, B = MI()
fact100 = [1, 2, 4, 5, 10, 20, 25, 50, 100]
print("Yes" if bisect.bisect_left(fact100, A) != bisect.bisect_right(fact100, B) else "No")