import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import heapq

N, M = MI()
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C, D = MI()
	# コストに木を含める
    G[A].append([B, C * 10000 - D])
    G[B].append([A, C * 10000 - D])

INF = 10 ** 10
kakutei = [ False ] * (N + 1)
cur = [ INF ] * (N + 1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while len(Q) >= 1:
	# 次に確定させるべき頂点を求める
	# タプルにheapqで要素の0番目(現在までのコスト)で最小を考える
	pos = heapq.heappop(Q)[1]

	# Q の最小要素が「既に確定した頂点」の場合
	if kakutei[pos] == True:
		continue
	
	# cur[x] の値を更新する
	kakutei[pos] = True
	for e in G[pos]:
		if cur[e[0]] > cur[pos] + e[1]:
			cur[e[0]] = cur[pos] + e[1]
			heapq.heappush(Q, (cur[e[0]], e[0]))

# 答えを出力
trees = ((cur[N] // 10000 + 1) * 10000 - cur[N])
dist = (cur[N] + trees) // 10000
print(dist, trees)