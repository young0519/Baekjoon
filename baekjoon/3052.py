numArr = []


for i in range(10):
    a = int(input())
    numArr.append(a % 42)

result = list(set(numArr))


print(len(result))
