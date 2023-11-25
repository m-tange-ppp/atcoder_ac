import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
import heapq
N, Q = MI()
A = LI()
dic = defaultdict(int)
for a in A:
    dic[a] += 1

now = -1
heap = []
heapq.heapify(heap)
for j in range(N + 1):
    if dic[j] == 0:
        heapq.heappush(heap, j)
        if now < 0:
            now = j

for _ in range(Q):
    i, x = MI()
    maenox = dic[x]
    old = A[i - 1]
    dic[old] -= 1
    dic[x] += 1
    A[i - 1] = x

    if dic[old] == 0:
        heapq.heappush(heap, old)
        
    if dic[old] == 0 and old < now:
        now = old
    elif dic[now] != 0:
        while True:
            a = heapq.heappop(heap)
            if dic[a] == 0:
                now = a
                heapq.heappush(heap, a)
                break
        
    print(now)