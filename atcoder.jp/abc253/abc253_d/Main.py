import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, A, B = MI()
num_a = N // A
num_b = N // B
a = A
b = B
while b > 0:
    a, b = b, a % b
lcm = A * B // a
num_lcm = N // lcm
sum_n = N * (N + 1) // 2
sum_a = A * num_a * (num_a + 1) // 2
sum_b = B * num_b * (num_b + 1) // 2
sum_lcm = lcm * num_lcm * (num_lcm + 1) // 2
print(sum_n - sum_a - sum_b + sum_lcm)