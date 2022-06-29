# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# 문제 해결 생각
# 2진수를 str로 입력 받은후, int로 바꾸어 list로 만든다.
# 이후, 10진수로 바꿔준 후 다시 8진수로 바꿔준다.
import sys

ten_number = 0
count = 0
answer = ''
list1 = list(map(str,sys.stdin.readline()))
list1.pop() # \n 널문자 제거
list1 = list(map(int,list1))

# 10진수 만들기
for i in range(len(list1)): # [1, 1, 0, 1] 이면 len(list1) = 4
    count = len(list1) - i
    ten_number += (2**(count - 1)) * list1[i]

remainder = 0
# 10진수를 8진수 만들기
while (ten_number != 0):
    answer += str(ten_number%8)
    ten_number = ten_number // 8

answer = answer[::-1]
print(answer)

# int()에 ,를 찍고 뒤에
# 숫자를 넣으면 그 진법의 숫자를 받는다는 것
# oct는 8진법을 의미
# 따라서, 2진법으로 받은 숫자를 8진법으로 변환
# 10진법이 아니라 8진법을 나타내는 2글자를 숫자 앞에 넣음
# 따라서 [2:] 의 과정이 필요
print(oct(int(input(),2))[2:])
# 1101 = 2^3 + 2^2 + 2^0
# i = 0 -> count = 4, 첫번째 1 = 2^3 = 2 ^ (count - 1)
# i = 1 -> count = 3, 두번째 1 = 2^2 = 2 ^ (count - 1)
