import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

import math

T = I()
L, X, Y = MI()
Q = I()

def pos(E):
    return (0, L / 2 * math.cos(- E / T * 2 * math.pi + 3 / 2 * math.pi), L / 2 * math.sin(- E / T * 2 * math.pi + 3 / 2 *math.pi) + L / 2)

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

target = (X, Y, 0)

for _ in range(Q):
    E = I()
    p = pos(E)
    print(math.degrees(math.atan2(p[2], dist(target, (0, p[1], 0)))))
