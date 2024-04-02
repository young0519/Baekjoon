'''
구현 로직

N (데이터 개수) A(데이터 리스트, 단 클래스를 데이터로 담는 리스트)

for N만큼 반복 : 
	A 리스트 저장

A 리스트 정렬

for N 만큼 반복 : 
	A[i]의 정렬전 index - 정렬 후 index 계산의 최댓값을 찾아 저장

최댓값 + 1을 정답으로 출력'''

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N) : 
    A.append((int(input()), i))

max = 0

sorted_A = sorted(A)

for i in range(N) : 
    if max < sorted_A[i][1] - i : 
        max = sorted_A[i][1] - i

print(max + 1)
