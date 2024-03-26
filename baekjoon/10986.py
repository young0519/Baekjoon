"""
Pseudo code

n 입력받기 (수열의 개수) 
m 입력받기 (나누어떨어져야 하는 수) 
A 입력받기 (원본 수열 저장 리스트) 
S 선언하기 (합 배열)
C 선언하기 (같은 나머지의 인덱스를 카운트 하는 리스트)
answer 선언하기 (정답 변수)

for i -> 1 ~ n-1 : 
    S[i] = S[i-1] + A[i]   # 합 배열 저장

for i -> 0 ~ n-1 : 
    remainder = S[i] % M   # 합 배열을 M으로 나는 나머지 값
    if (remainder == 0) 정답을 1 증가
    C[remainder]의 값을 1 증가

for i -> 0 ~ m-1 : 
    C[i] (i가 나머지인 인덱스의 개수)에서 2가지를 뽑는 경우의 수를 정답에 더하기
    # C[i] 중 2개를 뽑는 경우의 수 계산 공식 C[i] * (C[i] - 1)/2
    
결과값 (answer) 출력


""" 
import sys 
input = sys.stdin.readline

n, m = map (int, input().split())
A =list(map(int, input().split()))  # 기존의 리스트

S = [0] * n                         # 합 배열 
C = [0] * m                         # 나머지의 인덱스를 카운트하는 배열
answer = 0                          # 결과값

for i in range(n) : 
    S[i] = S[i-1] + A[i]

for i in range(n) : 
    remainder = S[i] % m   # 합 배열을 M으로 나는 나머지 값
    if (remainder == 0) : 
        answer += 1
    C[remainder] += 1

for i in range(m) : 
    remainder = C[i] * (C[i] - 1)/2
    answer = answer + remainder

print(int(answer))