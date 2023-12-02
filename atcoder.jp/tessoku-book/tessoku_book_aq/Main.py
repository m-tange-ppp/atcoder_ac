import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,L = MI()
X = [LS() for _ in range(N)]
ans = 0
for i in range(N):

    if X[i][1] == "E":
        ans = max(ans,L-int(X[i][0]))
    else:
        ans = max(ans,int(X[i][0]))
print(ans)