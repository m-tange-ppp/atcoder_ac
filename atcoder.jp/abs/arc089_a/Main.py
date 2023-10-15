n = int(input())
points = [(0, 0, 0)]
f = True

for _ in range(n):
    points.append(tuple(map(int, input().split())))

for i in range(n):
    t = abs(points[i][0] - points[i + 1][0])
    x = abs(points[i][1] - points[i + 1][1])
    y = abs(points[i][2] - points[i + 1][2])
    if not (t % 2 == (x + y) % 2 and x + y <= t) :
        f =False
        break

if f:
    print("Yes")
else:
    print("No")