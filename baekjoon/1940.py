"""
n 입력 받기 (재료의 개수)
m 입력 받기 (갑옷 제작 재료 필요 개수)
stuffArr 입력 받기 (갑옷 제작 재료)

sort() 이용하여 stuffArr 정렬

두 포인터 사용
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
stuffArr = sorted(list(map(int, input().split())))

count = 0
i=0
j=n-1

while i < j: #투포인터이동원직따랴포인터를이동하며처리 
    if stuffArr[i] + stuffArr[j] < m:
        i += 1
    elif stuffArr[i] + stuffArr[j] > m:
            j -= 1
    else : 
         count += 1
         i += 1
         j -= 1

print(count)