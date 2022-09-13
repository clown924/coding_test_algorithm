# 주어진 수 N개 중에서
# 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())
numbers = list(map(int,input().split()))
count = 0

def is_prime_number(a):
    flag = True
    if a == 1:
        return False
    for i in range(2,a):
        if a % i == 0:
            flag = False
            break
        else:
            flag = True

    return flag

for number in numbers:
    if is_prime_number(number):
        count += 1
        continue

print(count)
