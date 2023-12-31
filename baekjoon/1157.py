str = input().upper()
strArray = list(str)

strCount = {}


for alpa in strArray:
    if alpa in strCount:
        strCount[alpa] += 1
    else:
        strCount[alpa] = 1

maxWord = [k for k, v in strCount.items() if max(strCount.values()) == v]

if len(maxWord) > 1:
    print("?")
else:
    print("".join(maxWord))
