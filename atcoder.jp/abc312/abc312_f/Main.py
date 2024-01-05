import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
T0 = []
T1 = []
T2 = []
for _ in range(N):
    T, X = MI()
    if T == 0:
        T0.append(X)
    elif T == 1:
        T1.append(X)
    else:
        T2.append(X)
T0.sort(reverse=True)
T1.sort()
T2.sort()
T0_sum = [0] * (M + 1)
for i in range(M):
    if i < len(T0):
        T0_sum[i + 1] = T0_sum[i] + T0[i]
    else:
        T0_sum[i + 1] = T0_sum[i]
# print(T0_sum)
T1_sum = [0] * (M + 1)
cnt = 0
for i in range(M):
    x = 0
    if cnt == 0:
        if T2:
            cnt = T2.pop()
    else:
        cnt -= 1
        if T1:
            x = T1.pop()
    T1_sum[i + 1] = T1_sum[i] + x
# print(T1_sum)
ans = 0
for i in range(M + 1):
    if ans < T0_sum[i] + T1_sum[M - i]:
        ans = T0_sum[i] + T1_sum[M - i]
print(ans)