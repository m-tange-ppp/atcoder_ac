import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
B = LI()

dp = [0] * N
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

ans = []
place = N
while True:
    ans.append(place)
    if place == 1:
        break
    if dp[place - 2] + A[place - 2] == dp[place - 1]:
        place -= 1
    else:
        place -= 2
ans.reverse()
print(len(ans))
print(*ans)