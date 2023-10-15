N, M = map(int, input().split())
tabetas = list(input().split())
colors = list(input().split())
values = list(map(int, input().split()))
sum = 0

for tabeta in tabetas:
    flag = True
    for i, color in enumerate(colors):
        if flag and tabeta == color:
            sum += values[i + 1]
            flag = False
    if flag:
        sum += values[0]

print(sum)