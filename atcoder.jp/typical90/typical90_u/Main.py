import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

from math import factorial
from sys import setrecursionlimit

setrecursionlimit(10 ** 7)

def comb(n, k):
    if n < k:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def rec(now: int):
    if seen[now]:
        return
    seen[now] = 1
    for n_node in edge[now]:
        if seen[n_node]:
            continue
        rec(n_node)
    post_order.append(now)
    return

def rec_re(now: int):
    global cnt
    if seen[now]:
        return
    seen[now] = 1
    for n_node in re_edge[now]:
        if seen[n_node]:
            continue
        rec_re(n_node)
    cnt += 1
    return

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
re_edge = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(lambda n: int(n) - 1, input().split())
    edge[x].append(y)
    re_edge[y].append(x)

# SCCのために強連結成分同士のトポロジカルソートをする
# つまり、テキトーな頂点からDFSをして帰りがけの順を記録する。これを全ての頂点を記録するまで行う
seen = [0] * N
post_order = []
for i in range(N):
    rec(i)

ans = 0
seen = [0] * N
for i in post_order[::-1]:
    cnt = 0
    rec_re(i)
    # 現在のatcoderのpypyだとmath.combが使えないのでcomb関数は自作
    ans += comb(cnt, 2)

print(ans)