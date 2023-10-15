import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = I()
Cs = LI()
Cs.sort()

a,b = 0,0
c = min(N // Cs[2], 9999)
my_min = 10 ** 9

for i in range(0, c + 1):
    a = min((N - Cs[2] * i) // Cs[0], 9999)
    for j in range(0, a + 1):
        if (N - Cs[2] * i - Cs[0] * j) % Cs[1] == 0:
            b = (N - Cs[2] * i - Cs[0] * j) // Cs[1]
            if j + b + i < my_min:
                my_min = j + b + i

print(my_min)