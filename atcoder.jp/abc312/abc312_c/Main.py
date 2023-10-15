import sys
from collections import deque
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

import bisect

n,m = MI()
a = LI()
b = LI()

left = -1
right = 10 ** 9 + 1

def check(x):
    counta = 0
    countb = 0
    for sell in a:
        if sell <= x:
            counta += 1
    for buy in b:
        if buy >= x:
            countb += 1
    if counta >= countb:
        return True
    else:
        return False

while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)