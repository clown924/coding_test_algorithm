# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션
# 골드바흐의 추측 :
# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

# 골드바흐의 추측 알고리즘
# 소수1 + 소수2 = N 이므로 N - 소수1 = 소수2
# j가 소수이면 number - j도 소수이다.
# 이를 이용

r = 1000000
check = [True for _ in range(r)]
for i in range(2,int(r**0.6)):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False
import sys
T = int(input())

for i in range(T): # 입력 받은 수가 소수인지
    number = int(sys.stdin.readline())
    count = 0
    if number == 0:
        break
    for j in range(2,(number//2)+1):
        if check[j] == True: # j가 소수이고
            if check[number-j] == True: # number - j가 소수이면
                count += 1
    print(count)
