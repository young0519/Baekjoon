'''
!!!구현 로직!!!

N (수열 개수) A (수열 리스트)
A 수열 리스트 채우기

for N만큼 반복 : 
	if 현재 수열값 >= 오름차순 자연수 : 
		while 현재 수열값 >= 오름차순 자연수 : 
			append()
			오름차순 자연수 1 증가
			(+) 저장
		pop()
		(-) 저장
	else 현재 수열 값 < 오름차순 자연수 : 
		pop()
		if 스택 pop 결과값 > 수열의 수 :
			NO 출력
		else : 
			(-) 저장
	
if NO값을 출력한 적이 없으면 : 
	저장한 값 출력
'''

'''
시간 초과된 로직
N = int(input())
A = [0] * N

for i in range(N) : 
    A[i] = int(input())

// 시간 복잡도 : O(n)

stack = []
num = 1
Result = True
answer = ""

for i in range(N) : 
    su = A[i]
    if su >= num : 
        while su >= num : 
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else :
        n = stack.pop()
        if n > su : 
            print("NO")
            Result = False
            break
        else : 
            answer += "-\n"
            
if Result : 
    print(answer)
'''

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)