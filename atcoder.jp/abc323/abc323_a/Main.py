import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
flag = True
for i in range(1, 9):
    if S[2 * i - 1] == "1":
        flag = False
        break
print("Yes") if flag else print("No")