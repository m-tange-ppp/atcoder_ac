import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [ord(c) for c in list(input().strip())]
my_str = ""
count = 0

for i in range(K, 0, -1):
    min = 10000
    min_index = 0
    for j in range(count, N - i + 1):
        if min > S[j]:
            min = S[j]
            min_index = j
    my_str += chr(min)
    count = min_index + 1

print(my_str)