import sys
input=sys.stdin.readline

H, W = map(int, input().split())
num_list = []
row_list = []
enum_list = []
column_list = [0]*W
sum_list = [[0]*W for _ in range(H)]

for _ in range(H):
    num_list.append(list(map(int, input().split())))

for i in range(H):
    row_list.append(sum(num_list[i]))

for j in range(W):
    for i in range(H):
        column_list[j] += num_list[i][j]

for i in range(H):
    for j in range(W):
        sum_list[i][j] = row_list[i] + column_list[j] - num_list[i][j]

for lst in sum_list:
    out = " ".join(map(str, lst))
    print(out)