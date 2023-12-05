import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
E = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = MI()
    E[a].append(b)
    E[b].append(a)
for i in range(1, N + 1):
    e = set(E[i])
    if len(e) == 0:
        print(f"{i}: {{}}")
    else:
        print(f"{i}: {e}")