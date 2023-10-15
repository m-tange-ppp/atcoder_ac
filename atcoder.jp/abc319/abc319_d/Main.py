import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
L = LI()
for l in range(N):
  L[l] += 1

l = max(L)-1
r = sum(L)
while l+1 < r:
  mid = (r+l)//2
  rows = 1
  left_words = mid
  for i in range(len(L)):
    if (left_words >= L[i]):
      left_words -= L[i]
    else:
      rows += 1
      left_words = mid
      left_words -= L[i]
  if(rows > M):
    l = mid
  else:
    r = mid
print(r-1)