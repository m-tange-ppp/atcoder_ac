import sys
input=sys.stdin.readline

n =  int(input())
mylist = list(map(int, input().split()))
for i in range(0, len(mylist), 7):
    sublist = mylist[i:i+7]
    sum = 0
    for a in sublist:
        sum += a
    print(sum)