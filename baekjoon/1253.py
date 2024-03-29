"""

N(데이터 개수)
Result(좋은 수 개수 저장 변수)
A(수 데이터 저장 리스트)
A 리스트 정렬

for N만큼 반복:
	변수 초기화(찾고자 하는 값 find =A[k], 포인터 i, 포인터 j) 
	while i <j:
		if A [ i ] + A [ j ] == find :
			두 포인터 i, j가 k가 아닐 때 좋은 수 개수 1 증가 및 while 문 종료
			두 포인터 i나 j가 k가 맞을 때 포인터 변경 및 계속 수행 
		elif A[i] + A[j] <find: 포인터 i 증가
		else: 포인터 j 감소
		
좋은 수 개수 출력

"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

result = 0

for k in range(N) : 
    find = A[k]
    i = 0
    j = N-1

    while i < j : 
        if A[i] + A[j] == find:
		    if i != k and j != k : 
				result += 1
				break
			
			elif i == k :
				i += 1
				
			elif j == k : 
				j -= 1
				
		elif A[i] + A[j] < find : 
			i += 1
		else : 
			j -= 1            

print(result)