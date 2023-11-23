import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

a, b = MI()
keta = []
strb = str(b)
MOD = 10 ** 9 + 7
ans = 1
for i in range(len(strb)):
    mul = a ** (int(strb[i]))
    for _ in range(len(strb) - 1 - i):
        mul = mul ** 10 % MOD
    ans = ans * mul % MOD
print(ans)
    
    
        