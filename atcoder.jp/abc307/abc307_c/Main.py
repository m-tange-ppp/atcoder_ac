import sys
input=sys.stdin.readline

def convert(H, W, S):
    s = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s.add((i, j))
    return s

def normalize(s):
    if s == {}:
        return s
    my = min(y for (y, x) in s)
    mx = min(x for (y, x) in s)
    return set((y - my, x - mx) for (y, x) in s)

def slide(s, i, j):
    if s == {}:
        return s
    return set((y + i, x + j) for (y, x) in s)

HA, WA = map(int, input().split())
A = normalize(convert(HA, WA, [input() for _ in range(HA)]))
HB, WB = map(int, input().split())
B = normalize(convert(HB, WB, [input() for _ in range(HB)]))
HX, WX = map(int, input().split())
X = normalize(convert(HX, WX, [input() for _ in range(HX)]))

istrue = False

if not istrue:
    for i in range(-HX, HX):
        for j in range(-WX, WX):
            if normalize(slide(A, i, j).union(B)) == X:
                istrue = True
print("Yes" if istrue else "No")
