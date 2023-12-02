import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
import math
N = II()
A = LI()
dic = defaultdict(int)
for a in A:
    dic[a] += 1
ans = 0
for v in dic.values():
    if v >= 3:
        ans += math.comb(v, 3)
print(ans)