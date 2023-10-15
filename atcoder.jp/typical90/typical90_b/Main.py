n = int(input())

s_list = [""]
gen_list = []
choices = []

for s in s_list:
    if len(s) == n:
        point = 0
        for i in range(n):
            if point < 0:
                break
            elif s[i] == "(":
                point += 1
            else:
                point += -1
        if point == 0:
            print(s)
    if len(s) == n + 1:
        break
    s_list.append(s + "(")
    s_list.append(s + ")")
