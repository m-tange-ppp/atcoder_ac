import sys
input = sys.stdin.readline

balls1 = list(list(map(int, input().split())) for _ in range(30))

movelist1 = []

def trade(i, j, I, J):
    if balls1[i][j] < balls1[I][J]:
        c = balls1[i][j]
        balls1[i][j] = balls1[I][J]
        balls1[I][J] = c
        movelist1.append(" ".join(map(str, [i, j, I, J])))

def up(i, j):
    if i == 0:
        return
    elif j == 0:
        trade(i, j, i - 1, j)
        up(i - 1, j)
    elif j == i:
        trade(i, j, i - 1, j - 1)
        up(i - 1, j - 1)
    else:
        if balls1[i - 1][j] > balls1[i - 1][j - 1]:
            trade(i, j, i - 1, j)
            up(i - 1, j)
        else:
            trade(i, j, i - 1, j - 1)
            up(i - 1, j - 1)

for n in range(465):
    for i in range(30):
        for j, num in enumerate(balls1[i]):
            if n == num:
                up(i, j)

print(len(movelist1))
for move in movelist1:
    print(move)