import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque

Q = II()
query = [input().split() for _ in range(Q)]
queue = deque()

for q in query:
    t = int(q[0])
    if t == 1:
        queue.append(q[1])
    elif t == 2:
        print(queue[0])
    else:
        queue.popleft()