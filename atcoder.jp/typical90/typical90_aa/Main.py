import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
user_set = set()
for i in range(N):
    user = s()
    if not user in user_set:
        print(i + 1)
        user_set.add(user)