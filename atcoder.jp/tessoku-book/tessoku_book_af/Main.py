import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, A, B = MI()
flag = True
dp = [True] * (N+1)
for i in range(N+1):
    if i >= A and dp[i-A] == False:
        dp[i] = True
    elif i >= B and dp[i-B] == False:
        dp[i] = True
    else:
        dp[i] = False
print("First" if dp[N] else "Second")