# Q1
from re import I


def is_odd(num):
    if num % 2 == 1:
        print("홀수입니다.")
    else :
        print("짝수입니다.")

is_odd(3)
is_odd(4)

# Q2
def average_all(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(average_all(2,4,6,8,10))
print(average_all(1,2,3,4,5))

# Q3
#input1 = input("첫번째 숫자를 입력하세요:")
#input2 = input("두번째 숫자를 입력하세요:")

#total = int(input1) + int(input2)
#print("두 수의 합은 %s 입니다" % total)

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt","r")
read = f2.readline()
print(read)
f2.close()

# Q6
f3 = open("test2.txt","a")
f3.write(input("아무것이나 입력하세요: "))

# Q7
f4 = open("test3.txt","r")
body = f4.read()
f4.close()

body = body.replace("java","python")
f4 = open("test3.txt","w")
f4.write(body)
f4.close()