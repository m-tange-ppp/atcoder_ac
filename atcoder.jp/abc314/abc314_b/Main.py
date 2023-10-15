import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n = I()
clist = []
alist = []
for _ in range(n):
    clist.append(I())
    alist.append(LI())
x = I()

ans = []
for index, nums in enumerate(alist):
    if x in nums:
        ans.append((index, clist[index]))
ans1 =  [elem[0] + 1 for elem in list(filter(lambda x: x[1] == min(ans, key=lambda x:x[1])[1], ans))]

if ans1:
    print(len(ans1))
    print(*ans1)
else:
    print(0)