import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque

N = II()
A = LI()
ans = [0] * N
level2 = deque()
for i in range(N):
	if i >= 1:
		level2.append((i, A[i - 1]))
		while len(level2) >= 1:
			kabuka = level2[-1][1] # 株価はタプルの 2 番目の要素
			if kabuka <= A[i]:
				level2.pop()
			else:
				break
	if len(level2) >= 1:
		ans[i] = level2[-1][0] # 日付はタプルの 1 番目の要素
	else:
		ans[i] = -1
print(*ans)