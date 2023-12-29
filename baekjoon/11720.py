sum = 0  # 숫자의 총 합
N = int(input())
numString = list(map(int, list(input())))

for i in range(N):
    sum += numString[i]

print(sum)
