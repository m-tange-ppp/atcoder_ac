import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
med = list(LI() for _ in range(N))
med.sort(key=lambda x:x[0], reverse=True)

my_sum = 0
count = 0
for a in med:
    my_sum += a[1]

if my_sum > K:
    while my_sum > K:
        data = med.pop()
        my_sum -= data[1]
    print(data[0] + 1)
else:
    print(1)
