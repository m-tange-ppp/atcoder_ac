import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import Counter

T = II()

def prime_factorize(n):
    if n == 1:
        return [1]
    else:
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        a.sort()
        return a

for _ in range(T):
    C = II()
    pf_c = Counter(prime_factorize(C))
    if len(pf_c) == 1:
        print("No")
    else:
        print("Yes")