import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7) 
from collections import deque
from collections import defaultdict
N = II()
slimes = defaultdict(int)
sizes = deque()
for _ in range(N):
    S, C = MI()
    slimes[S] = C
    sizes.append(S)
ans = 0

def merge(k):
    global ans
    num = slimes[k]
    count = 2 * (num // 2)
    if count != 0:
        slimes[k] = num - count
        slimes[2 * k] += count // 2
        sizes.append(2 * k)

while sizes:
    q = sizes.pop()
    merge(q)
print(sum(slimes.values()))