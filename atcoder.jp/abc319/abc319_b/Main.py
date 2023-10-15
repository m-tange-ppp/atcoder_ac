import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
fact_list = []
for i in range(1, 10):
    if N % i == 0:
        fact_list.append(i)

ans = []
for i in range(N + 1):
    flag = True
    for f in fact_list:
        if i % (N // f) == 0:
            ans.append(f)
            flag = False
            break
    if flag:
        ans.append("-")

print("".join(map(str,ans)))