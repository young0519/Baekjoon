'''
!! 구현 로직 !!
N (수열 개수) A (수열 리스트) ans (정답 리스트)
A 수열 리스트 채우기
myStack (스택 선언)

for i를 N만큼 반복 : 
	while 스택이 비지 않고, 현재 수열값이 top에 해당하는 수열보다 클 때까지 : 
		스택에서 pop한 값을 index로 하는 정답 리스트 부분을 수열 리스트의 현재 값(A[i])으로 저장
	스택에 i의 값을 저장
	
while 스택이 빌 때까지 : 
	스택에 있는 index의 정답 리스트에 -1 저장

정답 리스트 출력
'''

# 시간 초과된 코드
n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n) : 
    # 스택이 비어있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while myStack and A[myStack[-1]] < A[i] : 
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack : 
    ans[myStack.pop()] = -1

result = ""

for i in range(n) : 
    result += str(ans[i]) + " "

print(result)

## 통과한 코드

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE= [-1]*N
stack = [0] # 0번 인덱스

for i in range(1, N):
    # 오큰수 : A[i]의 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽 값 
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i] # 해당 인덱스 칸은 A[i]
    stack.append(i)
print(*NGE)
