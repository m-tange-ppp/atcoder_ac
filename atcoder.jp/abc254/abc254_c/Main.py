import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
A = LI()
sorted_A = sorted(A)
group = [set() for _ in range(K)]
for i in range(N):
    group[i % K].add(A[i])
for i in range(N):
    if not sorted_A[i] in group[i % K]:
        print("No")
        sys.exit()
print("Yes")
