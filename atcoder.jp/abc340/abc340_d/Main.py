#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

import heapq

N = ii()
G = [ list() for i in range(N + 1) ]
for i in range(N - 1):
	a, b, x = mi()
	G[i + 1].append((i + 2, a))
	G[i + 1].append((x, b))

kakutei = [ False ] * (N + 1)
cur = [ inf ] * (N + 1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while Q:
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
print(cur[-1])