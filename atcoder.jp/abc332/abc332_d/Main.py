from operator import index
import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from itertools import permutations
import copy
H, W = MI()
A = [LI() for _ in range(H)]
B = [LI() for _ in range(H)]

trades_row = list(permutations([i for i in range(H)]))
trades_col = list(permutations([i for i in range(W)]))
# print(trades)
ans = 100
for r in trades_row:
    for c in trades_col:
        A_copy = copy.deepcopy(A)
        C = []
        for i in r:
            C.append(A_copy[i])
        # print(C)
        per = [i for i in range(W)]
        for j in range(W):
            if c[j] != per[j]:
                ind = per.index(c[j])
                per[j], per[ind] = per[ind], per[j]
                for i in range(H):
                    C[i][j], C[i][ind] = C[i][ind], C[i][j]
        if B == C:
            tento_r = 0
            for i in range(H - 1):
                for j in range(i + 1, H):
                    if r[i] > r[j]:
                        tento_r += 1
            tento_c = 0
            for i in range(W - 1):
                for j in range(i + 1, W):
                    if c[i] > c[j]:
                        tento_c += 1
            if ans > tento_r + tento_c:
                ans = tento_r + tento_c
if ans == 100:
    print(-1)
else:
    print(ans)