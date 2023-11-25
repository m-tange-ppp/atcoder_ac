import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
D = II()
ans = 10 ** 13
nijo = []
x = 0
while (x - 1) ** 2 <= D:
    nijo.append(x ** 2)
    x += 1
for i in range(len(nijo)):
    x2 = nijo[i]
    sa = abs(x2 - D)
    ind = bisect.bisect_left(nijo, sa)
    if ind == 0:
        kouho = x2 + nijo[ind]- D
    elif ind == len(nijo):
        kouho = x2 + nijo[ind - 1]- D
    else:
        kouho = min(abs(x2 + nijo[ind]- D), abs(x2 + nijo[ind - 1]- D))
    if kouho < ans:
        ans = kouho
print(ans)