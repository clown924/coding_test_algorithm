# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# ex) 8 = 3 + 5, 20 = 3 + 17 = 7 + 13
# ex) 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23

# 문제 해결 방법
# 에라토스네테스의 체를 이용해 소수만을 담은 리스트를 만들고,
# 가장 작은 소수(j) 부터 number보다 작지만 가장 큰 소수잉
# (number - j) 또한 소수인지 판별한다.
# 둘 다 소수라면 print하고, 아니라면
# 그 다음 소수 (j + 1) 과 number - (j + 1) 또한 소수인지
# 판별한다.
# 에라토스네테스의 체를 이용하는 이유는 소수인지 아닌지 확인하는
# 시간을 O(1) 로 줄이기 위해 사용한다.

# 처음 생각
# 소수만을 담은 리스트를 만들고, 기준이 되는 수보다 작은
# 소수들을 더해보며 만족하는지 찾음


r = 1000000
check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False
import sys

while(True): # 입력 받은 수가 소수인지
    number = int(sys.stdin.readline())
    if number == 0:
        break
    for j in range(3,r):
        if check[j] == True:
            if check[number-j] == True:
                print("%d = %d + %d"%(number, j, number - j))
                break
