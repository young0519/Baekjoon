N, X = input().split()

N = int(N)
X = int(X)
result = []
numArr = list(input().split())

for i in range(N):
    numArr[i] = int(numArr[i])

for i in numArr:
    if i < X:
        result.append(str(i))


resultStr = " ".join(result)
print(resultStr)
