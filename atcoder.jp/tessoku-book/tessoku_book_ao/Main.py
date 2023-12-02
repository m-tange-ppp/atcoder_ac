import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
S = SI()
for i in range(N-2):
    if S[i:i+3] == "RRR" or S[i:i+3] == "BBB":
        print("Yes")
        sys.exit()
print("No")