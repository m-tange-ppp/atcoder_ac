import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

K = II()
HH = str(21 + K // 60)
MM = "0" * (2 - len(str(K % 60))) + str(K % 60)
print(HH + ":" +  MM)