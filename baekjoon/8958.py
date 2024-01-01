T = int(input())
point = 1
resultArr = []


for i in range(T):
    quizArr = list(input())
    point = 1
    result = 0

    for quiz in quizArr:
        if quiz == "O":
            result = result + point
            point += 1
        elif quiz == "X":
            point = 1
    resultArr.append(result)
for i in resultArr:
    print(i)
