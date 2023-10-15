import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M, P = MI()
A = LI()
B = LI()
B.sort()
sum_B = []
for i in range(M):
    if i == 0:
        sum_B.append(B[i])
    else:
        sum_B.append(sum_B[i - 1] + B[i])
sum_B.insert(0, 0)
ans = 0

for a in A:
    l = -1
    r = M
    mid = (l + r) // 2
    while r - l > 1:
        mid = (l + r) // 2
        if a + B[mid] < P:
            l = mid
        else:
            r = mid
    ans += a * (l + 1) + sum_B[l + 1] + P * (M - l - 1)
print(ans)