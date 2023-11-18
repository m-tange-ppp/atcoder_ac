import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
N, M = MI()
A = LI()
dic = defaultdict(int)
dic[A[0]] = 1
print(A[0])
c = A[0]
for i in range(1, M):
    dic[A[i]] += 1
    if dic[A[i]] == dic[c] and A[i] < c:
        print(A[i])
        c = A[i]
    elif dic[A[i]] > dic[c]:
        print(A[i])
        c = A[i]
    else:
        print(c)