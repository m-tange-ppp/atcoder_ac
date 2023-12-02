import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,S,M,L = MI()
ans = 10 ** 7
for i in range(N//6 + 2):
    for j in range((N - 6*i)//8 + 2):
        for k in range((N - 6*i - 8*j)//12 + 2):
            if 6*i + 8*j + 12*k >= N:
                ans = min(ans, S*i + M*j + L*k)
print(ans)