import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

D, N = MI()
min_H = [0] + [24]*D
for _ in range(N):
    L,R,H = MI()
    for i in range(L, R+1):
        min_H[i] = min(min_H[i], H)
print(sum(min_H))