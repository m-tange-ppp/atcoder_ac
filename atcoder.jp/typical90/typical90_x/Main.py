import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, K = mi()
A = li()
B = li()
abs_sum = 0
for i in range(N):
    abs_sum += abs(A[i] - B[i])
print("Yes") if abs_sum <= K and abs_sum % 2 == K % 2 else print("No")