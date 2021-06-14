n = int(input())
flag = 1
for i in range(1, n + 1):
    j = 1
    for j in range(n + 1 - i):
        if flag == 1:
            print(1 , end = "")
        else:
            print(0 , end = "")
    print("")
    flag = not flag

