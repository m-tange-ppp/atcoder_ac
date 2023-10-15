import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
A = li()

MAX = 2 * 10 ** 5 + 1
x = [0] * MAX
for a in A:
    x[a] += 1

ans = 0
for i in range(1, MAX):
    j = 1
    while i * j < MAX:
        ans += x[i] * x[j] * x[i * j]
        j += 1
print(ans)