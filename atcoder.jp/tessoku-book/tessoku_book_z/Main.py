import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

Q = II()
for _ in range(Q):
    X = II()
    cnt = 2
    is_prime = True
    while cnt ** 2 <= X:
        if X % cnt == 0:
            is_prime = False
            break
        cnt += 1
    print("Yes" if is_prime else "No")