import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N = II()
A = LI()
A_ind = [[i,a] for i,a in enumerate(A)]
A_ind.sort(key=lambda x:x[1])
A_ind_v = [a[1] for a in A_ind]
A_sum = [[0,0]]*N
A_sum[0] = A_ind[0]
for i in range(1,N):
    A_sum[i] = [A_ind[i][0], A_sum[i-1][1] + A_ind[i][1]]
ans = []
for a in A_ind:
    i = bisect.bisect_right(A_ind_v, a[1]) - 1
    v = A_sum[-1][1] - A_sum[i][1]
    ans.append([a[0], v])
ans.sort(key=lambda x:x[0])
print(*[a[1] for a in ans])