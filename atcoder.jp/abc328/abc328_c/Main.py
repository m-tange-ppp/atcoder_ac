import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
S = SI()
Con = [0] * (N - 1)
for i in range(N - 1):
    if i == 0 and S[i] == S[i + 1]:
        Con[i] = 1
    else:
        Con[i] = Con[i - 1]
        if S[i] == S[i + 1]:
            Con[i] += 1
Con = [0] + Con
for _ in range(Q):
    l, r = MI()
    print(Con[r - 1] - Con[l - 1])
