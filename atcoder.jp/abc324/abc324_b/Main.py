import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
count2 = 0
count3 = 0
while True:
    if N % 2 == 0:
        N //= 2
    if N % 3 == 0:
        N //= 3
    if N % 2 != 0 and N % 3 != 0:
        break
print("Yes" if N == 1 else "No")