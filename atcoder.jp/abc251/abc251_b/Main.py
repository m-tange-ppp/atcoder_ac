import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from itertools import combinations

N, W = MI()
A = LI()
A.extend([0, 0])

ans = set()

for comb in combinations(A, 3):
    sum_comb = sum(comb)
    if sum_comb <= W:
        ans.add(sum_comb)

print(len(ans))