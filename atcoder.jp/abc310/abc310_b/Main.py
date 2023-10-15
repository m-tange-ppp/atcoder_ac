import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, M = MI()
my_list = []
for _ in range(N):
    my_list.append(LI())
my_list.sort(key=lambda x:(x[0], -x[1]))

def check(a, b):
    if all(el in a[2:] for el in b[2:]):
        if a[0] < b[0] or a[1] > b[1]:
            return True
    return False

f = False

for i in range(N - 1):
    if f:
        break
    for c in my_list[i + 1:]:
        if check(my_list[i], c):
            f = True
            break

print("Yes" if f else "No")