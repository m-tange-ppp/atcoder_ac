import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, X = MI()
c_first = 0
clear = []
for i in range(min(N, X)):
    A, B = MI()
    c_first += A + B
    clear.append(c_first + B * (X - i - 1))
print(min(clear))