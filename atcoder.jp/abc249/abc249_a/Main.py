import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

A, B, C, D, E, F, X = mi()
time_T = X
time_A = X
d_T = 0
d_A = 0

while time_T > 0:
    if time_T < A:
        d_T += time_T * B
        timeT = 0
    else:
        d_T += A * B
        time_T -= A
    time_T -= C
while time_A > 0:
    if time_A < D:
        d_A += time_A * E
        timeA = 0
    else:
        d_A += D * E
        time_A -= D
    time_A -= F
if d_T > d_A:
    print("Takahashi")
elif d_T < d_A:
    print("Aoki")
else:
    print("Draw")