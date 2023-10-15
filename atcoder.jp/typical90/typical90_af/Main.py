import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

from itertools import permutations
N = i()
A = [li() for _ in range(N)]
M = i()
NG = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = mi()
    NG[x - 1][y - 1] = NG[y - 1][x - 1] = 1

numbers = [i for i in range(N)]
perm_list = list(permutations(numbers))
max_time = 10 ** 5

for perm in perm_list:
    f = True
    sum_time = 0
    for i, order in enumerate(perm):
        sum_time += A[order][i]
        if i < N - 1 and f:
            l = perm[i]
            r = perm[i + 1]
            if NG[l][r] == 1:
                f = False
                break
    if f and sum_time < max_time:
        max_time = sum_time
if max_time == 10 ** 5:
    max_time = -1

print(max_time)