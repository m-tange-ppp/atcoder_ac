import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = SI()
def check(N):
    for i in range(len(N) - 1):
        if not int(N[i]) > int(N[i + 1]):
            print("No")
            return
    print("Yes")
    return
check(N)