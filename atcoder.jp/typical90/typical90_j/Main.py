N = int(input())
students = list(list(map(int, input().split()))for _ in range(N))
sums = [[0,0]]
s1 = 0
s2 = 0
for i in range(N):
    if students[i][0] == 1:
        s1 += students[i][1]
    else:
        s2 += students[i][1]
    sums.append([s1, s2])

Q = int(input())

for _ in range(Q):
    start, end =map(int, input().split())
    sum1 = sums[end][0] - sums[start - 1][0]
    sum2 = sums[end][1] - sums[start - 1][1]
    print(*(sum1, sum2))
