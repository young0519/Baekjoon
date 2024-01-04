# n % h = 나머지 = 층 수
# n // h = 몫 + 1 = 호수

T = int(input())  # 테스트 케이스 T
result = []

for i in range(T):
    H, W, N = input().split()
    H = int(H)  # 층 수 H
    W = int(W)  # 방 수 W
    N = int(N)  # N번 째 손님

    Y = N % H  # N번째 손님이 묵는 방의 층수 (나머지)
    X = N // H + 1  # N번째 손님이 묵는 방의 층수에서의 걸어나온 번호 (몫)

    # N % H = 나머지
    # N // H = 몫

    # 6 12 6  => 601 (나머지 = 0)
    # 6 12 12 => 602  (나머지 = 0)

    if Y == 0:
        if H == N:
            Y = H
            X = 1
        else:
            Y = H
            X = N // H

    # 층수와 번호를 더하기 위해 문자열화
    Y = str(Y)
    X = str(X)

    if len(X) == 1:
        X = "0" + X

    result.append(Y + X)

for i in result:
    print(int(i))
