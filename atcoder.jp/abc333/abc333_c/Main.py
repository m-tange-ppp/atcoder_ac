import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect 
repu = [1]
for i in range(120):
    repu.append(repu[-1] * 10 + 1)
N = II()
ans = []
c = 0
i = 0
j = 0
k = 0
while c < 340:
    ans.append(repu[i] + repu[j] + repu[k])
    if i == j == k:
        i, j, k = 0, 0, k + 1
    elif i == j:
        i, j = 0, j + 1
    else:
        i += 1    
    c += 1
print(ans[N - 1])