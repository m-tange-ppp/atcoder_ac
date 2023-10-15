import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
S = []
for _ in range(N):
    S.append(SI())
nums = [str(i) for i in range(10)]
ans = 10 **4
for num in nums:
    stop = [0] * N
    for i in range(N * 10):
        for j in range(N):
            if S[j][i % 10] == num and stop[j] == 0:
                stop[j] = 1
                if sum(stop) == N and i < ans:
                    ans = i
                break

print(ans)