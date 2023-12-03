import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
Q = II()
stack = deque()
for _ in range(Q):
    q = LS()
    t = int(q[0])
    if t == 1:
        stack.append(q[1])
    elif t == 2:
        print(stack[-1])
    else:
        stack.pop()