hour, min = input("").split()

hour = int(hour) * 60  # 시 단위를 분 단위로 변경
min = int(min)

beforeTime = hour + min

afterTime = beforeTime - 45

if afterTime < 0:
    hour = afterTime // 60 + 24
    min = 60 - (45 - min)

else:
    hour = afterTime // 60
    min = afterTime % 60

print(hour, min)
