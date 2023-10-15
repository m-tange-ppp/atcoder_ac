import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
A = li()
min_a = 1001
max_a = 0
sum_a = 0
for a in A:
    sum_a += a
    if a < min_a:
        min_a = a
    elif a > max_a:
        max_a = a
print((N + 1) * (2 * min_a + N) // 2 - sum_a)
