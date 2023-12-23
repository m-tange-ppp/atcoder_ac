import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
A = LI()
if K == 1:
    print(0)
    sys.exit()
ans = 0
l = 0
r = K - 1
if K % 2 == 0:
    while r - l > 0:
        al = A[l + 1] - A[l]
        ans += al
        l += 2
else:
    f_sum = []
    for i in range(1, K, 2):
        if i == 1:
            f_sum.append(A[i] - A[i - 1])
        else:
            f_sum.append(f_sum[-1] + A[i] - A[i - 1])
    b_sum = []
    for i in range(K - 1, 0, -2):
        if i == K - 1:
            b_sum.append(A[i] - A[i - 1])
        else:
            b_sum.append(b_sum[-1] + A[i] - A[i - 1])
    ans = 10 ** 9
    for i in range(K // 2 + 1):
        l = i - 1
        r = K // 2 - i - 1
        if l < 0:
            kouho = b_sum[r]
        elif r < 0:
            kouho = f_sum[l]
        else:
            kouho = f_sum[l] + b_sum[r]
        if kouho < ans:
            ans = kouho
print(ans)