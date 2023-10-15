import sys
from functools import cmp_to_key

def cmp(a, b):
    if a[1] * b[2] == b[1] * a[2]:
        return 0
    return 1 if a[1] * b[2] < b[1] * a[2] else -1

input = sys.stdin.readline

N = int(input())
members = []

for i in range(N):
    A, B = map(int, input().split())
    members.append((i + 1, A, A + B))

members.sort(key=cmp_to_key(cmp))

result = [m[0] for m in members]
print(*result)