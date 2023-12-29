N = int(input())  # 정수의 개수

numString = input()  # 공백을 포함한 N개의 정수
numArray = numString.split()  # N개의 문자열을 포함한 배열

for i in range(N):
    numArray[i] = int(numArray[i])

print(min(numArray), max(numArray))
