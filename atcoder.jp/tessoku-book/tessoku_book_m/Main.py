import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
A = LI()
A.append(10 ** 9 + 1)
ans = 0
for i in range(N - 1):
    l = i
    r = N
    while r - l > 1:
        mid = (l + r) // 2
        if A[mid] - A[i] <= K:
            l = mid
        else:
            r = mid
    ans += l - i
print(ans)