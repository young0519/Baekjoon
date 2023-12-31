numArray = []
countNum = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}

for i in range(3):
    a = int(input(""))
    numArray.append(a)

result = list(str(numArray[0] * numArray[1] * numArray[2]))
for num in result:
    if num in result:
        countNum[num] += 1
    else:
        countNum = 0

for i in countNum.keys():
    print(countNum[i])
