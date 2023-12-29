numArray = []

for i in range(9):
    a = int(input(""))
    numArray.append(a)

print(max(numArray))
print(numArray.index(max(numArray)) + 1)
