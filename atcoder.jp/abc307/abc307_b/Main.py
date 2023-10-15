import sys
import itertools
input=sys.stdin.readline

n =  int(input())
all_false = True

def check(w):
    for i in range(len(w)):
        if w[i] != w[len(w)-1 -i]:
            return False
    return True

lines = []
for _ in range(n):
    lines.append(input().strip())
perms = list(itertools.permutations(lines, 2))
result = []
for perm in perms:
    result.append("".join(perm))

for word in result:
    if check(word):
        print("Yes")
        all_false = False
        break
if all_false:
    print("No")