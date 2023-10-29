import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
while True:
    a = int(str(N)[0])
    b = int(str(N)[1])
    c = int(str(N)[2])
    if a * b == c:
        print(100 * a + 10 * b + c)
        break
    else:
        N += 1