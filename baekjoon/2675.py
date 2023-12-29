T = int(input())  # 테스트 케이스 개수
rArray = []
sArray = []
all = []
for i in range(T):
    string = input()
    all = string.split()
    rArray.append(int(all[0]))
    sArray.append(all[1])

for i in range(T):
    count = rArray[i]
    string = sArray[i]
    strArray = list(string)

    for i in range(len(strArray)):
        strArray[i] = count * strArray[i]

    a = ("").join(strArray)
    print(a)
