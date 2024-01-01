import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N = II()
H = LI()
dp = [0] * N
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(H[i - 2] - H[i]), dp[i - 1] + abs(H[i - 1] - H[i]))
# print(dp)
ans = [N]
stack = deque()
stack.append(N)
while stack:
    s = stack.pop() - 1
    if s >= 2 and dp[s] == dp[s - 2] + abs(H[s - 2] - H[s]):
        stack.append(s - 1)
        ans.append(s - 1)
    elif s >= 1 and dp[s] == dp[s - 1] + abs(H[s - 1] - H[s]):
        stack.append(s)
        ans.append(s)
print(len(ans))
print(*ans[::-1])