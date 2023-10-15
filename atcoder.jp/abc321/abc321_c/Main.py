import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

K = II()
nums = [[] for _ in range(10)]
nums[0] = [i for i in range(10)]
c = 1
while c < 10:
    for n in nums[c - 1]:
        now = 10 * n
        last = int(str(n)[len(str(n)) - 1])
        for j in range(0, last):
            nums[c].append(now + j)
    c += 1
ans = []
for i in range(10):
    ans += nums[i]
print(ans[K])
