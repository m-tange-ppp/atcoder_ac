import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
table = [list(input().strip()) for _ in range(H)]

name = "snuke"
stack = deque()
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = [[-1]*W for _ in range(H)]
if table[0][0] == "s":
    dist[0][0] = 0
    stack.append([0, 0])

while stack:
    y1, x1 = stack.popleft()
    for dy, dx in dir:
        y2 = y1 + dy
        x2 = x1 + dx
        if not(0 <= y2 <= H - 1 and 0 <= x2 <= W - 1):
            continue
        if dist[y2][x2] == -1 and name[(dist[y1][x1] + 1)% 5] == table[y2][x2]:
            dist[y2][x2] = dist[y1][x1] + 1
            stack.append([y2, x2])

print("Yes" if dist[H - 1][W - 1] != -1 else "No")