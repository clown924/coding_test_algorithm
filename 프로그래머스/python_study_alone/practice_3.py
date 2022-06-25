# Q2 : while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

from re import I


i = 1
result = 0
while i <= 1000 :
    if i % 3 == 0:
        result += i
    i += 1
print(result)

# Q3
i = 1
while i <= 5:
    print(i*'*')
    i += 1

# Q4
for i in range(1,101):
    print(i)

# Q5
List1 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for i in List1:
    result += i
print(result / len(List1))

# Q6
numbers = [1,2,3,4,5]
result = [num * 2 for num in numbers if num % 2 == 1 ]
print(result)