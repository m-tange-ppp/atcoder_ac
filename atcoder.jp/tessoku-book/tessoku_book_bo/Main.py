import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, c = map(int, input().split())

    graph[u].append((v, c)) # u->vの辺
    graph[v].append((u, c)) # v->uの辺

# プリム法
# 頂点がマークされているか確認する配列
marked = [False for _ in range(N + 1)]

# マークされている頂点数を数える
marked_cnt = 0

# はじめに0頂点をマーク
marked[1] = True
marked_cnt += 1

# heap
q = []

# 頂点0に隣接する辺を保存
for j, c in graph[1]:
    heapq.heappush(q, (c, j))

total = 0

# すべての頂点をマークするまでwhileループ
while marked_cnt < N:
    # 最小の重みの辺をheapで取り出す
    c, i = heapq.heappop(q)

    # マークされているならスキップ
    if marked[i]:
        continue

    # 頂点をマーク
    marked[i] = True
    marked_cnt += 1

    total += c

    # 頂点iに隣接する辺を保存
    for j, c in graph[i]:
        # マークされていればスキップ
        if marked[j]:
            continue

        heapq.heappush(q, (c, j))

print(total)