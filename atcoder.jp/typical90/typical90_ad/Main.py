import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, K = mi()
num_prime_factor = [0] * (N + 1)

for i in range(2, N + 1):
    if num_prime_factor[i] != 0:
        continue
    for j in range(i, N + 1, i):
        num_prime_factor[j] += 1

ans = 0
for n in num_prime_factor:
    if n >= K:
        ans += 1

print(ans)